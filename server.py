from SocketServer import ThreadingTCPServer, BaseRequestHandler, TCPServer
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
        self.data = self.request.recv(1024).strip().decode('UTF-8')
        print "{} wrote:".format(self.client_address[0])
        data = loads(self.data)
        print(data)
        # just send back the same data, but upper-cased
        self.request.sendall(dumps({'return': data['packages']}))

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 8888

    # Create the server, binding to localhost on port 9999
    server = TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()

