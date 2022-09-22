from django.urls import path
from Transacciones.views import TransListView

#secrea el archivo urls para trabajabar  contrlar de una marnera mas comoda y ordenada las rutas

urlpatterns = [
    path('transaccion', TransListView.as_view(), name='Lista Transacciones'),
]