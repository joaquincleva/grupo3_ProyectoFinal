from django import forms
from .models import Noticia

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'contenido', "categoria", "imagen"]

class Form_Alta(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ('titulo', 'contenido', "categoria", "imagen")
