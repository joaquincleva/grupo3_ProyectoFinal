from django.db import models

# Create your models here.
class Noticia(models.Model):
    titulo = models.CharField(max_length=30)
    autor = models.CharField(max_length=31)
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    contenido = models.TextField(max_length=4000)

    def __str__(self):
        return self.titulo