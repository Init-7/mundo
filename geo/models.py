# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.gis.db import models

class world(models.Model):
    fips = models.CharField(max_length=2)
    iso2 = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)
    un = models.IntegerField()
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.BigIntegerField()
    region = models.IntegerField()
    subregion = models.IntegerField()
    lon = models.FloatField()
    lat = models.FloatField()
    geom = models.PolygonField(srid=4326)

    def __unicode__(self):
        return u"%s %s" % (self.iso2, self.name)

