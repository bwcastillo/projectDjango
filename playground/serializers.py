from rest_framework import serializers
from .models import Sensors

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