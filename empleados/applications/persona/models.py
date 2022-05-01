from django.db import models
from django.forms import ImageField
from applications.departamento.models import Departamento

# Create your models here.


class Empleado(models.Model):
    """ MODELO PARA CADA EMPLEADO """

    JOB_CHOICES = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro'),
    )
    # contador
    # administrador
    # Economista
    # otro
    first_name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    job = models.CharField('Trabajo', max_length=50, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    # FIELDNAME = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return str(self.id) + ' - ' + self.first_name + ' - ' + self.last_name
