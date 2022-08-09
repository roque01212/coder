from pyexpat import model
from django.db import models

# Create your models here.

class Familia(models.Model):
    Sex_choises=(
        ('0', 'Hombre'),
        ('1', 'Mujer'),
        ('2', 'otro'),
    )
    type_family_chises=(
    ('0', 'Padre'),
    ('1', 'Madre'),
    ('2', 'Hijo'),
    ('3', 'Cuñao'),
    )

    nombre = models.CharField('Nombre: ', max_length=20)
    apellido = models.CharField('Apellido', max_length=10)
    edad = models.PositiveIntegerField()
    sexo = models.CharField('Sexo', max_length=1, choices=Sex_choises)
    parentezco = models.CharField('Parentezco Familiar:', max_length=1, choices=type_family_chises)
    dni = models.CharField('DNI:', max_length=10)
    fecha_nac = models.DateField('Fecha Nacimiento: ', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Zapas(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    precio = models.IntegerField()
    fecha_v = models.DateField('Fecha venta', auto_now=False, auto_now_add=False)

    
class Mascotas(models.Model):
    Sex_choises=(
        ('0', 'Macho'),
        ('1', 'Hembra'),
    )
    nombre = models.CharField('Nombre: ',max_length=20)
    raza = models.CharField('Raza: ',max_length=20)
    edad = models.PositiveIntegerField()
    fecha_nac = models.DateField('Fecha Nacimiento: ', blank=True, null=True) 
    sexo = models.CharField('Sexo', max_length=1, choices=Sex_choises)
