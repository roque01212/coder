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
    )

    nombre = models.CharField('Nombre: ', max_length=20)
    apellido = models.CharField('Apellido', max_length=10)
    edad = models.PositiveIntegerField()
    sexo = models.CharField('Sexo', max_length=1, choices=Sex_choises)
    parentezco = models.CharField('Parentezco Familiar:', max_length=1, choices=type_family_chises)
    dni = models.CharField('DNI:', max_length=10)
#    fecha_nac = models.DateTimeField('Fecha Nacimiento: ', auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


    