from django.shortcuts import render
from django.views.generic import ListView
from .models import Empleado

def home(request):
    Emp=Empleado.objects.all()
    #Emp=Empleado.objects.all()[:5] muestra la cantidad de objetos definida en los corchetes
    #Emp=Empleado.objects.all()[4:6]muestra la cantidad de objetos definida en los corchetes segun su posicion
    #Emp=Empleado.objects.all().order_by('id') # se ordena segun el id en este caso de menor a mayor
    #Emp=Empleado.objects.all().order_by('id','nombre') # se ordena segun el idy el nombre en este caso de menor a mayor
    #Emp=Empleado.objects.all().order_by('-id') # se ordena segun el id en este caso de mayor a menor
    #Emp=Empleado.objects.filter(empresa='',nombre='')#filtra por nombre de empresa que se defina y nombre
    #Emp=Empleado.objects.filter(id__gte=4)#filtra por id mayores a los id por ensima del numero definido
    #Emp=Empleado.objects.filter(id__lte=4)#filtra por id menores a los id por ensima del numero definido
    #verificar esta informacion Djandoproyect.com buscar documentation order_by y entrar a queryset pai referer
    #Emp=Empleado.objects.filter(nombre__startwith='A')#filtra por todos los nombres que inicien con la letra A
    #Emp=Empleado.objects.filter(nombre__contains='e')#filtra por nombres que contengan la letra e
    data={
            'titulo':'Lista Transacciones',
            'Usuarios': Emp
        }
    return render(request, "listarEmple.html", data)

class EmpListView (ListView):
    model=Empleado
    template_name='listarEmple.html'



     

    
