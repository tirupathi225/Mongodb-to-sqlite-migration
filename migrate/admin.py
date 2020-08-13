from django.contrib import admin
from migrate.models import SectorsClass, GeoClass
# Register your models here.

class SectorsClassAdmin(admin.ModelAdmin):
    list_display = ['sectorName', 'sector_id']

class GeoClassAdmin(admin.ModelAdmin):
    list_display = ['countryName', 'countryCode', 'geo_id', 'countryCurrency']


admin.site.register(SectorsClass, SectorsClassAdmin)
admin.site.register(GeoClass, GeoClassAdmin)