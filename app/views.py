from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import Group, User
from django.http import HttpResponse
from app.models import Package,Catalog
from app.forms  import PostFormUpgradeHost
from json import dumps
from datetime import datetime

# Create your views here.
def index(request):
  queryset = Package.objects.all()
  return render_to_response('overview.html', locals(), context_instance=RequestContext(request))


def data(request):
  mimetype = 'application/json'
  if request.GET:
    try:
      hostname = request.GET['hostname']
      udata  = Package.objects.filter(title=hostname)
    except:
      udata    = Package.objects.all()
  else:
    udata    = Package.objects.all()
  sdata    = []
  for d in udata:
    data = {'id': d.id, 'hostname': d.title, 'ip': d.ip , 'packages': d.packages }
    sdata.append(data)
  return HttpResponse(dumps(sdata), mimetype)

def catalogData(request):
  mimetype = 'application/json'
  if request.GET:
    try:
      hostname = request.GET['hostname']
      udata    = Catalog.objects.filter(title=hostname)
    except:
      udata    = Catalog.objects.all()
  else:
      udata    = Catalog.objects.all()
  sdata    = []
  for d in udata:
    data = {'id': d.id, 'hostname': d.title, 'message': d.message, 'ip': d.ip , 'packages': d.packages }
    sdata.append(data)
  return HttpResponse(dumps(sdata), mimetype)


def hostname_page(request, slug):
  packages = Package.objects.filter(slug=slug)
  data = [x for x in packages.values()[0]['packages'].split()]
  packagelistform = PostFormUpgradeHost(data)
#  packagelistform.fields['packages'].choices = [(x.packages, x) for x in packages.values()[0]]
  packagelistform.fields['packages'].choices = [x for x in packages.values()[0]['packages'].split()]
  data = {"packagelistform": packagelistform.fields['packages'].choices,}
  return render_to_response("hostname.html", locals(), context_instance=RequestContext(request))


def LogMessageCatalog(hostname,message):
  obj = Catalog.objects.filter(title=hostname)
  if obj:
    obj.update(message='%s : %s ' % (message, str(datetime.now())))
    return 0
  return 1


def generateCatalog(request):
  packages  = request.POST.getlist('packagelist[]')
  hostname  = request.POST['hostname']
  ip        = request.POST['ip']
  try:
    obj = Catalog.objects.filter(title=hostname)
    if obj:
      updated_packages = obj.update(packages=packages,ip=ip)
      if updated_packages:
        LogMessageCatalog(hostname, 'Successfully updated')
    else:
      obj = Catalog(title=hostname,packages=packages,ip=ip,slug=hostname)
      obj.save()
      LogMessageCatalog(hostname,'Successfully created')
  except Catalog.DoesNotExist:
      obj = Catalog(title=hostname,packages=packages,ip=ip,slug=hostname)
      obj.save()
      LogMessageCatalog(hostname, 'Successfully created')

  return HttpResponse(packages)
