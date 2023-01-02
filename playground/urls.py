from django.urls import path
from . import views

urlpatterns = [
    #path('hello/', views.say_hello)
    path('', views.SensorsListAPIView.as_view(), name='sensors_list'),
    path('<int:id>/', views.SensorsRetrieveAPIView.as_view(), name='sensors_detail'),
    path('create/', views.SensorsCreateAPIView.as_view(), name='sensors_create'),
    path('update/<int:id>/', views.SensorsRetrieveUpdateAPIView.as_view(), name='sensors_update'),
    path('delete/<int:id>/', views.SensorsDestroyAPIView.as_view(), name='sensors_delete'),
    path('home/', views.sensorpost, name="home"),
    path('showform/', views.showform, name='showform'),
    path('getform/', views.getform, name='getform'),
    path("sensor_location/", views.sensorLocation, name='sensorlocationapi'),
    path(r'sensorupdatedelete/<int:pk>/', views.sensorUpdateDelete, name="sensor_updatedelete")
]