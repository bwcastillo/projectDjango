from django.db import models
from django.contrib.gis.db import models


# Create your models here.

class Sensors(models.Model):
    sensor_type = models.CharField(max_length=200, blank=False)
    address = models.CharField(max_length=400, blank=False)
    date = models.DateField()
    time = models.DateTimeField()
    measure = models.FloatField(max_length=10)
    coordinates = models.PointField(srid=4326, null=True, blank=True, )
    unit = models.CharField(max_length=10)
    user_id = models.CharField(max_length=200, blank=False)


def __str__(self):
    return "{}, {}".format(self.user_id, self.address) #It allows to show clearly in app about the details
