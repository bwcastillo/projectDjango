from django.urls import path
from . import views

urlpatterns = [
    #path('hello/', views.say_hello)
    path('', views.SensorsListAPIView.as_view(), name='sensor_list'),
]