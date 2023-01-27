from django.contrib import admin

# Register your models here.

from .models import Houses, Lands

from .models import HouseImages, LandImages


admin.site.register([Houses, Lands])

admin.site.register([HouseImages, LandImages])
