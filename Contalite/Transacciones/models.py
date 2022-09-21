from django.db import models
from Empleados.models import Empleado

#creamos los modelos de las tablas que vamos a usar

class Transaccion(models.Model):
    id_tr=models.AutoField(auto_created=True,unique=True,primary_key=True)
    tipo=models.CharField("Ingreso - Egreso",max_length=50,null=False)
    fecha_tr=models.DateField(auto_now=True)
    usuario=models.ForeignKey(Empleado,related_name="transaccion", on_delete=models.CASCADE)
    concepto=models.TextField("Concepto",max_length=500,null=False) 
    monto=models.IntegerField("Monto",null=False) 
    

    def __str__(self):
        return "%s id_tr:" % self.id_tr

