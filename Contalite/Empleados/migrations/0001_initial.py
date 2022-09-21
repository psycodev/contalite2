# Generated by Django 4.1 on 2022-09-21 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id_empleado', models.AutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('nom_emp', models.CharField(max_length=25, verbose_name='Nombres')),
                ('ape_emp', models.CharField(max_length=25, verbose_name='Apellidos')),
                ('nom_usu', models.CharField(max_length=20, unique=True, verbose_name='Nombre Usuario')),
                ('password', models.CharField(max_length=50, verbose_name='Password')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='E-mail')),
                ('telefono', models.CharField(max_length=10, verbose_name='Telefono')),
                ('fecha_creacion', models.DateField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('admin', models.BooleanField(null=True, verbose_name='Rol')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Empresa', to='Empresas.empresa')),
            ],
        ),
    ]
