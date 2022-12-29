# Create your views here.
from rest_framework import generics
from .serializers import SensorsListSerializer, SensorsDetailSerializer
from .models import Sensors
from django.shortcuts import render
from django.http import HttpResponse


def say_hello(request):
    #return HttpResponse('Hello World')
    return render(request, 'hello.html', {'name': 'Bryan'})

#LIST
class SensorsListAPIView(generics.ListAPIView):
    queryset = Sensors.objects.all()
    serializer_class = SensorsListSerializer

#RETRIEVE
class SensorsRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Sensors.objects.all()
    serializer_class = SensorsDetailSerializer

#CREATE
class SensorsCreateAPIView(generics.CreateAPIView):
    queryset = Sensors.objects.all()
    serializer_class = SensorsDetailSerializer

#RETRIEVE AND UPDATE
class SensorsRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = "id"
    queryset = Sensors.objects.all()
    serializer_class = SensorsDetailSerializer

#DESTROY
class SensorsDestroyAPIView(generics.DestroyAPIView):
    lookup_field = "id"
    queryset = Sensors.objects.all()

#CREATING VIEWS HTTP REQUEST RESPONSE
def sensorpost(request):
    path = request.path
    response = HttpResponse("This works!")
    return response

def showform(request):
    return render(request, "form.html")

def getform(request):
    if request.method == "POST":
        sensor_type=request.POST['sensor_type']
        address=request.POST['address']
        date=request.POST['date']
        time=request.POST['time']
        measure=request.POST['measure']
        unit=request.POST['unit']
        user_id=request.POST['user_id']
    return HttpResponse("Sensor Type:{} Address:{} Date:{} Time:{} Measure:{} Unit:{} UserID:{}".format(sensor_type,address,date,time,measure,unit,user_id))