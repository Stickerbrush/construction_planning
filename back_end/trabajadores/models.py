from django.db import models

# Create your models here.

class trabajadores(models.Model):
    
    trabajador_id = models.BigAutoField(primary_key=True,)
    trabajador_nombre = models.CharField(max_length=50)
    trabajador_apellido = models.CharField(max_length=50)
    trabajador_documento = models.CharField(max_length=20)
    trabajador_direccion = models.CharField(max_length=50)
    trabajador_celular = models.CharField(max_length=15)
    trabajador_contrasena= models.CharField(max_length=256)
    trabajador_estado = models.IntegerField()

    class Meta:
        db_table = "trabajadores"
