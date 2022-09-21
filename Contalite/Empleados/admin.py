from django.contrib import admin
from .models import Empleado


#en esta seccion registramos los modelos que deban ser usados por el admin
admin.site.register(Empleado)
