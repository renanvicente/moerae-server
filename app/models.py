from django.db import models

# Create your models here.
class Package(models.Model):
  '''Hostname and packages'''
  title    = models.CharField( max_length=100, )
  ip       = models.CharField( max_length=100, )
  packages = models.TextField(  )
  slug     = models.SlugField(  )

  def __unicode__(self):
    return u'%s' % self.title


class Catalog(models.Model):
  '''Hostname and packages'''
  title    = models.CharField( max_length=100, )
  message  = models.TextField(  )
  ip       = models.CharField( max_length=100, )
  packages = models.TextField(  )
  slug     = models.SlugField(  )

  def __unicode__(self):
    return u'%s' % self.title

