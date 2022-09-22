from tabnanny import verbose
from django.db import models
from Empresas.models import Empresa
from .choices import roles

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
    rol=models.CharField("Rol", max_length=20, choices=roles, default= 'Administrador')

    class Meta:
        verbose_name='Empleados'
        verbose_name_plural='Empleados'
        db_table='Empleados'
        ordering=['ape_emp','nom_emp']

        #muestra los datos de cada empleado
    def nombreCompleto(self):
        return "{} {}, Id: {} ".format(self.ape_emp, self.nom_emp, self.id_empleado)
    def __str__(self):
        return self.nombreCompleto()
    #con el meta podremos trabajar los metadatos de cada modelo

"""    def __str__(self):
        return "%s id_empleado:" % self.id_empleado"""


    
    
    

