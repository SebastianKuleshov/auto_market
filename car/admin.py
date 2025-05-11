from django.contrib import admin
from . import models

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'milage', 'year', 'location', 'price')
    search_fields = ('brand__name', 'model')
    list_filter = ('year', 'brand')

admin.site.register(models.Car, CarAdmin)
