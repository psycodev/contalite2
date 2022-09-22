from django.contrib import admin
from users.views import registro_user
from django.urls import path


urlpatterns = [
        path('usu', registro_user.as_view(), name='Lista Transacciones'),
    ]
