# Create your views here.
from rest_framework import generics
from .serializers import SensorsListSerializer, SensorsDetailSerializer
from .models import Sensors
from django.shortcuts import render
from django.http import HttpResponse


def say_hello(request):
    #return HttpResponse('Hello World')
    return render(request, 'hello.html', {'name': 'Bryan'})

class SensorsListAPIView(generics.ListAPIView):
    queryset = Sensors.objects.all()
    serializer_class = SensorsListSerializer

class SensorsRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Sensors.objects.all()
    serializer_class = SensorsDetailSerializer

class SensorsCreateAPIView(generics.CreateAPIView):
    queryset = Sensors.objects.all()
    serializer_class = SensorsDetailSerializer