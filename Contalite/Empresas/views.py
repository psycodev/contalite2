from django.shortcuts import render
from django.views.generic import ListView
from .models import Empresa

def home(request):
    Empr=Empresa.objects.all()
    data={
            'titulo':'Lista Empresa',
            'Usuarios': Empr
        }
    return render(request, "listarEmp.html", data)

class EmpreListView (ListView):
    model=Empresa
    template_name='listarEmp.html'



     

    
