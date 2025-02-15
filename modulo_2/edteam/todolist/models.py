from django.db import models

# Create your models here.
class Tarea(models.Model):

    Estado_choises=(
        ('1','pendiente'),
        ('2','terminado')
        )
    descripcion=models.CharField(max_length=200)
    fecha_registro=models.DateField(auto_now_add=True)
    estado=models.CharField(max_length=1,choices=Estado_choises)