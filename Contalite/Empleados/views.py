from django.shortcuts import render
from django.views.generic import ListView
from .models import Empleado

def home(request):
    Emp=Empleado.objects.all()
    data={
            'titulo':'Lista Transacciones',
            'Usuarios': Emp
        }
    return render(request, "listarEmple.html", data)

class EmpListView (ListView):
    model=Empleado
    template_name='listarEmple.html'



     

    
