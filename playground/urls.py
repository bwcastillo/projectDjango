from django.urls import path
from . import views

urlpatterns = [
    #path('hello/', views.say_hello)
    path('', views.SensorsListAPIView.as_view(), name='sensor_list'),
    path('<int:id>/', views.SensorsRetrieveAPIView.as_view(), name='sensors_detail'),
    path('create/',views.SensorsCreateAPIView.as_view(),name='pizzeria_create')
]