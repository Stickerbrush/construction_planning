from django.db import models

# Create your models here.

class obras(models.Model):
    
    obra_id = models.BigAutoField(primary_key=True,)
    obra_nombre = models.CharField(max_length=50)
    obra_direccion = models.CharField(max_length=50)
    obra_ciudad = models.CharField(max_length=50)
    obra_estado = models.IntegerField()
    obra_latitud = models.DecimalField(max_digits=8, decimal_places=6)
    obra_longitud = models.DecimalField(max_digits=8, decimal_places=6)

    class Meta:
        db_table = "obras"
