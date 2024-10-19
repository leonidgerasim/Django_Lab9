from django.contrib import admin
from .models import Employee, Driver, Automobile, Waybill

# Register your models here.

admin.site.register(Employee)
admin.site.register(Driver)
admin.site.register(Automobile)
admin.site.register(Waybill)
