from django.urls import path
from Empleados.views import EmpListView

#secrea el archivo urls para trabajabar  contrlar de una marnera mas comoda y ordenada las rutas

urlpatterns = [
    path('empleados', EmpListView.as_view(), name='Lista Empleados'),
]