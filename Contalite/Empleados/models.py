from django.db import models
from Empresas.models import Empresa

#creamos los modelos de las tablas que vamos a usar

class Empleado (models.Model):
    id_empleado=models.AutoField(auto_created=True,unique=True,primary_key=True)
    nom_emp=models.CharField("Nombres",null=False, max_length=25)    
    ape_emp=models.CharField("Apellidos",null=False,max_length=25)
    nom_usu=models.CharField("Nombre Usuario",unique=True, max_length=20, null=False)
    password=models.CharField("Password",max_length=50, null=False)
    email=models.EmailField("E-mail",unique=True,null=False,max_length=100)
    telefono=models.CharField("Telefono",null=False,max_length=10)
    empresa=models.ForeignKey(Empresa, related_name='Empresa', on_delete=models.CASCADE)
    fecha_creacion=models.DateField(auto_now=True)
    image = models.ImageField(null=True, blank=True)
    admin=models.BooleanField("Rol", null=True)

    def __str__(self):
        return "%s id_empleado:" % self.id_empleado

