from django.contrib import admin
from .models import *
# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display= ['name','age','test','B2B_price','status','B2C_price','B2C_Status']


admin.site.register(Patient,PatientAdmin)

# 'date'