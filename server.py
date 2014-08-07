# Declare the settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moerae.settings")

from SocketServer import ThreadingTCPServer, BaseRequestHandler, TCPServer
from app.models import Package
from json import loads, dumps



class TCPServer(ThreadingTCPServer):
  allow_reuse_address = True

class MyTCPHandler(BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        data = loads(self.data)
        print "Received from '%s': %s \n" % (self.client_address[0], data)
        list_packages = ""
        for package in data['packages']:
          if list_packages == "":
            list_packages += package
          else:
            list_packages += " " + package
        print(list_packages)
        # just send back the same data, but upper-cased
        self.request.sendall(dumps({'return': data['packages']}))
        try:
          obj = Package.objects.filter(title=data['hostname']).update(ip=data['ip'],packages=list_packages,slug=data['hostname'])
          if obj:
            self.request.sendall(dumps({'return':'Successfully updated'}))
          else:
            obj = Package(title=data['hostname'],ip=data['ip'],packages=list_packages,slug=data['hostname'])
            obj.save()
            self.request.sendall(dumps({'return':'Successfully created'}))
        except Package.DoesNotExist:
            obj = Package(title=data['hostname'],ip=data['ip'],packages=list_packages,slug=data['hostname'])
            obj.save()
            self.request.sendall(dumps({'return':'Successfully created'}))

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 8888

    # Create the server, binding to localhost on port 8888
    server = TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()

