# Generated by Django 4.1 on 2022-09-22 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Transacciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccion',
            name='tipo',
            field=models.CharField(choices=[('Ingreso', 'Ingreso'), ('Egreso', 'Egreso')], default='Elija una opcion', max_length=20, verbose_name='tipo'),
        ),
    ]
