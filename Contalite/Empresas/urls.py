from django.urls import path
from Empresas.views import EmpreListView

#secrea el archivo urls para trabajabar  contrlar de una marnera mas comoda y ordenada las rutas

urlpatterns = [
    path('empresa', EmpreListView.as_view(), name='Lista Empresas'),
]