from django.contrib import admin

# Register your models here.
from core.models.cars import Brand,Car
admin.site.register(Brand)
admin.site.register(Car)