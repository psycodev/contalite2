from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegistrationForm

class registro_user(CreateView):
    model = User
    template_name= "registrar.html"
    form_class=RegistrationForm

    
    
    