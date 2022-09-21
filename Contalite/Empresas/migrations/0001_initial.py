# Generated by Django 4.1 on 2022-09-21 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('nit', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('direccion', models.CharField(max_length=100, verbose_name='Direccion')),
                ('fecha_creacion_emp', models.DateField(auto_now=True)),
                ('nom_emp', models.CharField(max_length=25, verbose_name='Nombre Empresa')),
                ('sec_prod', models.CharField(max_length=25, verbose_name='Senctor Productivo')),
                ('ciudad', models.CharField(max_length=100, verbose_name='Ciudad')),
                ('telefono', models.CharField(max_length=100, verbose_name='Telefono')),
            ],
        ),
    ]
