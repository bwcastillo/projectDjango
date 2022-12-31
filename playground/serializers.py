#import rest_framework_gis.serializers
from rest_framework import serializers
from .models import Sensors
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class SensorsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensors
        fields = [
            "id",
            "sensor_type",
            "address",
            "date",
        ]

class SensorsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensors
        fields = [
            "id",
            "sensor_type",
            "address",
            "date",
            "time",
            "measure",
            "coordinates",
            "unit",
            "user_id"
        ]

class SensorsDetailLocationSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Sensors
        geo_field = "coordinates"
        fields = [
            "id",
            "sensor_type",
            "address",
            "date",
            "time",
            "measure",
            "coordinates",
            "unit",
            "user_id"
        ]