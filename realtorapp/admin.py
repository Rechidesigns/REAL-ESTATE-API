from django.contrib import admin

# Register your models here.

from .models import Houses, Lands

admin.site.register([Houses, Lands])
