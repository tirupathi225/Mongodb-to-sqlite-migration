from rest_framework import serializers
from . models import GeoClass
from rest_framework.serializers import ValidationError
from .models import SectorsClass


class GeoSerializer(serializers.ModelSerializer):
	class Meta:
		model = GeoClass
		fields='__all__'
class SectorSerializer(serializers.ModelSerializer):
	class Meta:
		model = SectorsClass
		fields='__all__'
