from django.urls import path
from Users.views import UserListView

#secrea el archivo urls para trabajabar  contrlar de una marnera mas comoda y ordenada las rutas

urlpatterns = [
    path('', UserListView.as_view(), name='Lista usuarios'),
]