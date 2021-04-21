from django.db import models

# Create your models here.

class clientes(models.Model):
    
    cliente_id = models.BigAutoField(primary_key=True,)
    cliente_nombre = models.CharField(max_length=50)
    cliente_nit = models.CharField(unique=True,max_length=10)
    cliente_estado = models.IntegerField()
    cliente_correo = models.EmailField(max_length=50)
    cliente_direccion = models.CharField(max_length=50)
    cliente_contrasena = models.CharField(max_length=256)

    class Meta:
        db_table = "clientes"
