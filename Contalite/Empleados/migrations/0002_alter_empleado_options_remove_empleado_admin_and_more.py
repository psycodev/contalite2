# Generated by Django 4.1 on 2022-09-21 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Empleados', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['ape_emp', 'nom_emp'], 'verbose_name': 'Empleados', 'verbose_name_plural': 'Empleados'},
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='admin',
        ),
        migrations.AddField(
            model_name='empleado',
            name='rol',
            field=models.CharField(choices=[('Administrador', 'Administrador'), ('Empleado', 'Empleado')], default='Administrador', max_length=20, verbose_name='Rol'),
        ),
        migrations.AlterModelTable(
            name='empleado',
            table='Empleados',
        ),
    ]