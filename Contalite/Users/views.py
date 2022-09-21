from django.shortcuts import render
from django.views.generic import ListView
from .models import User

def home(request):
    listausers=User.objects.all()
    data={
            'titulo':'Lista usuarios',
            'Usuarios': listausers
        }
    return render(request, "listarUser.html", data)

class UserListView (ListView):
    model=User
    template_name='listarUser.html'



     

    
