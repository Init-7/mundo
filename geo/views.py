# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from djgeojson.serializers import Serializer as GeoJSONSerializer
from django.http import HttpResponse
from .models import world #usar mayuscula sorry

def paises(request):
    paises = world.objects.all()
#    contenidos = []

    data = GeoJSONSerializer().serialize(paises, use_natural_keys=True, with_modelname=False)

    return HttpResponse(data)

def pais(request, aidi):
    pais = world.objects.get(id = aidi)
    #Agregar envio de centro para el mapa
    lat = pais.geom.centroid.y
    lon = pais.geom.centroid.x
    return render(request, 'geo/pais.html',{'qs_results': pais,
                                             'latitude':lat,
                                             'longitude': lon}
                 )

