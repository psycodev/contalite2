from cProfile import label
from pyexpat import model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    
    class Meta: 
        model= User
        fields=[
            'username',
            'first_name',
            'last_name',
            'email',
            'is_superuser',
            'is_staff',
        ]
        labels ={
            'username':'Nombre de usuario',
            'first_name':'Nombre',
            'last_name':'Apellido',
            'email':'E-mail',
            'is_superuser':"Amnistrador",
            'is_staff':'staff',


        }
