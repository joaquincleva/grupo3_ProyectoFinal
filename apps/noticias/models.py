from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nombre = models.CharField(max_length=80)
    
    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    titulo = models.CharField(default="",max_length=200)
    contenido = models.TextField(default="")
    fecha_publicacion = models.DateTimeField("created at",auto_now_add=True)
    fecha_modificacion = models.DateTimeField("modified at",auto_now=True)
    autor=models.ForeignKey(User,default="",on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria,default="", on_delete=models.CASCADE)
    imagen = models.ImageField(default="",upload_to="noticias")

    def MisComentarios(self):
        return self.comentario_set.all()

    def __str__(self):
        return self.titulo