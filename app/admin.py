from django.contrib import admin
from app.models import *

# Register your models here.
class PackageAdmin(admin.ModelAdmin):
  pass

admin.site.register(Package,PackageAdmin)
