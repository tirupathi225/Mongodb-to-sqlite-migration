from django.db import models
import json

class SectorsClass(models.Model):
    sectorName = models.CharField(max_length = 300)
    subsectors = models.CharField(max_length=200)
    sector_id = models.CharField(max_length=200)

    def set_subsectors(self, x):
        self.foo = json.dumps(x)

    def get_subsectors(self):
        return json.loads(self.foo)
    def __str__(self):
        return self.sectorName

class GeoClass(models.Model):
    countryName = models.CharField(max_length=200)
    countryCode = models.CharField(max_length=200)
    countryCurrency = models.CharField(max_length=200)
    cities = models.CharField(max_length=200)
    geo_id = models.CharField(max_length=200)
    
    
    def set_cities(self, x):
        self.foo = json.dumps(x)

    def get_cities(self):
        return json.loads(self.foo)
    def __str__(self):
        return self.countryName
    