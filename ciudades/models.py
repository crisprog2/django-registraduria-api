from django.db import models
from departamentos.models import TablaDepartamento

# Create your models here.
class TablaCiudad(models.Model):
    
    ciudad = models.TextField(blank=False)
    departamento = models.ForeignKey(TablaDepartamento, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.ciudad