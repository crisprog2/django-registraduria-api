from django.db import models

# Create your models here.
class TablaDepartamento(models.Model):
    
    departamento = models.TextField(blank=False)
    
    def __str__(self):
        return self.departamento