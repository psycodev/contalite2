from django.shortcuts import render
from django.views.generic import ListView
from .models import Transaccion

def home(request):
    Trans=Transaccion.objects.all()
    data={
            'titulo':'Lista Transacciones',
            'Usuarios': Trans
        }
    return render(request, "listarTrans.html", data)

class TransListView (ListView):
    model=Transaccion
    template_name='listarTrans.html'



     

    
