# Generated by Django 4.0.6 on 2022-08-08 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familia', '0004_familia_fecha_nac_alter_familia_parentezco'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascotas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre: ')),
                ('raza', models.CharField(max_length=20, verbose_name='Raza: ')),
                ('edad', models.PositiveIntegerField()),
                ('fecha_nac', models.DateField(blank=True, null=True, verbose_name='Fecha Nacimiento: ')),
                ('sexo', models.CharField(choices=[('0', 'Macho'), ('1', 'Hembra')], max_length=1, verbose_name='Sexo')),
            ],
        ),
    ]
