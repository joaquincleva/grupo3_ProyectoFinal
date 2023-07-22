from django.db import models
from django.utils import timezone

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateField(default=timezone.now)

    def __str__(self):
        return self.titulo