from django.contrib import admin
from django.contrib.gis import admin

# Register your models here.
from .models import Sensors

#Unregister the provided model admin:
from django.contrib.auth.models import User

from django.contrib.auth.admin import UserAdmin
@admin.register(User)
class NewAdmin(UserAdmin):
    pass

class LocationAdmin(admin.GeoModelAdmin):
    point_zoom = 3 #https://stackoverflow.com/questions/61611292/how-to-change-the-default-zoom-level-of-a-map-in-geodjangos-admin
    default_lat = 43.780918
    default_lon = -79.421371
    modifiable = True
    #map_template =  Interesting if I ref to OSM is just available in UTM and not geographic coords

admin.site.register(Sensors, LocationAdmin) #It will create a form for a Model in the admin interface
