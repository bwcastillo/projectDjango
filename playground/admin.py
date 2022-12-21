from django.contrib import admin

# Register your models here.
from .models import Sensors

admin.site.register(Sensors) #It will create a form for a Model in the admin interface