from django.db import models
from django.contrib.auth.models import User
from apps.noticias.models import Noticia


# Create your models here.
class Comentario(models.Model):
    fecha_publicacion = models.DateTimeField("created at", auto_now_add=True)
    fecha_modificacion = models.DateTimeField("modified at", auto_now=True)
    texto = models.TextField(max_length=1000)
    autor = models.ForeignKey(User, default="", on_delete=models.CASCADE)
    noticia = models.ForeignKey(Noticia, default="", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.autor}-{self.noticia}"