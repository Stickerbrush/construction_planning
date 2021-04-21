from django.db import models

# Create your models here.

class materiales(models.Model):
    
    material_id = models.BigAutoField(primary_key=True,)
    material_nombre = models.CharField(max_length=50)
    material_cantidad = models.IntegerField()
    material_estado = models.IntegerField()

    class Meta:
        db_table = "materiales"
