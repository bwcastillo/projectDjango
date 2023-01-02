# Create your views here.
from rest_framework import generics, status
from .serializers import SensorsListSerializer, SensorsDetailSerializer,SensorsDetailLocationSerializer
from .models import Sensors
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt #See what is this
from rest_framework.parsers import JSONParser #See what is this



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
@csrf_exempt
def sensorLocation(request):
    if request.method == 'GET':
        snippets = Sensors.objects.all()
        serializer = SensorsDetailLocationSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SensorsDetailLocationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def sensorUpdateDelete(request, pk):
    try:
        tutorial = Sensors.objects.get(pk=pk)
    except Sensors.DoesNotExist:
        return JsonResponse({'message': 'The sensor does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SensorsDetailLocationSerializer(tutorial, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tutorial.delete()
        return JsonResponse({'message': 'Sensor was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)