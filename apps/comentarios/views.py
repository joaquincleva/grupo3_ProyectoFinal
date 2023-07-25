from django.shortcuts import render, HttpResponseRedirect
from apps.noticias.models import Noticia
from apps.comentarios.models import Comentario
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import Form_Modificacion

# Create your views here.

def agregarComentario(request,noticia_id):
    comentario = request.POST.get("comentario", None)
    usuario = request.user
    noticia = Noticia.objects.get(id=noticia_id)
    Comentario.objects.create(texto=comentario, autor=usuario, noticia=noticia)
    return HttpResponseRedirect(reverse_lazy("noticias:detalle_noticia", kwargs={"noticia_id":noticia_id}))

class editar_comentario(UpdateView):
    model = Comentario
    form_class = Form_Modificacion
    template_name = 'comentarios/editar_comentario.html'
    success_url = reverse_lazy('noticias:lista_noticias')

class BorrarComentario(DeleteView):
    model = Comentario
    success_url = reverse_lazy('noticias:lista_noticias')
    # def get_success_url(self):
    #     reverse_lazy("noticias:detalle_noticia", kwargs={"noticia_id":self.request.noticia_id})