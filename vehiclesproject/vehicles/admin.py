from django.contrib import admin
from vehicles.models import Vehicle
# Register your models here.

class VehicleAdmin(admin.ModelAdmin):
    list_display = ['registration_number','image', 'model','brand','color','menufectured_date']

admin.site.register(Vehicle, VehicleAdmin)
