from django.db import models

# Create your models here.

class proveedores(models.Model):
    
    proveedor_id = models.BigAutoField(primary_key=True,)
    proveedor_nombre = models.CharField(max_length=50)
    proveedor_nit = models.CharField(unique=True,max_length=10)
    proveedor_direccion = models.CharField(max_length=50)
    proveedor_correo = models.EmailField(max_length=50)
    proveedor_celular = models.CharField(max_length=15)
    proveedor_estado = models.IntegerField()

    class Meta:
        db_table = "provedores"
