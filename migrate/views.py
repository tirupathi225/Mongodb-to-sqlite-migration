from django.shortcuts import render
import re
# from django.shortcuts import render
from . import models
from migrate.models import GeoClass, SectorsClass
from rest_framework import response, decorators,status
from rest_framework import viewsets
from migrate.serializers import GeoSerializer
from migrate.models import SectorsClass
from migrate.serializers import SectorSerializer
from django.template.response import TemplateResponse

# import requests
import urllib
from django.conf import settings
from django.http import JsonResponse,HttpResponse
from rest_framework.response import Response
import os

# Create your views here.
class GeoViewSet(viewsets.GenericViewSet):
    queryset = GeoClass.objects.filter() 
    serializer_class = GeoSerializer
    template_name = 'base.html'
    def list(self, request, *args, **kwargs):
        '''
            list works as GET method
        '''

        try:
            search_par = []
            for val in list(filter(None, str(request.build_absolute_uri()).split('/'))):
                if '=' in val:
                    search_par.append(val.split('=')[1])
            print(search_par)
        except:
            pass
        filter_country = GeoClass.objects.filter(countryName=search_par[0]).values()[0]
        filtered_cities = [val for val in eval(filter_country['cities']) if search_par[1].lower() in val.lower()]
        final_response =  [{'id':filter_country['id'], 'country_id':filter_country['countryCode'], 'name':val} for val in filtered_cities]
        return response.Response(final_response)


class SectorsViewSet(viewsets.GenericViewSet):
    queryset = SectorsClass.objects.filter() 
    serializer_class = GeoSerializer
    def list(self, request, *args, **kwargs):
        '''
            list works as GET method
        '''

        try:
            search_par = []
            for val in list(filter(None, str(request.build_absolute_uri()).split('/'))):
                if '=' in val:
                    search_par.append(val.split('=')[1])
            print(search_par)
        except:
            pass
        filter_sector = SectorsClass.objects.filter(sector_id=search_par[0]).values()[0]
        filtered_sectors = [val for val in eval(filter_sector['subsectors'])]
        final_response = [{'id':filter_sector['id'], 'sector_id':filter_sector['sectorName'], 'name':val} 
                    for val in filtered_sectors]


        return response.Response(final_response)
