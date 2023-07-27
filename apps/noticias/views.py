from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404, redirect
from .forms import Form_Modificacion, Form_Alta
from .models import Noticia,Categoria
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def catalogo(request):
    return render(request, 'noticias/catalogo.html')

# def crear_noticia(request):
#     if request.method == 'POST':
#         form = NoticiaForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('hola')
#     else:
#         form = NoticiaForm()
#     return render(request, 'noticias/crear_noticia.html', {'form': form})

class crear_noticia(LoginRequiredMixin,CreateView):
    model = Noticia
    form_class=Form_Alta
    template_name="noticias/crear_noticia.html"
    success_url=reverse_lazy("noticias:lista_noticias")
    
    def form_valid(self, form):
        noti=form.save(commit=False)
        noti.autor=self.request.user
        return super(crear_noticia,self).form_valid(form)


def lista_noticias(request):
    noticias = Noticia.objects.order_by('-fecha_publicacion')
    return render(request, 'noticias/listar_noticias.html', {'noticias': noticias})

class Categorias(ListView):
    model = Categoria
    template_name = "noticias/listar_categorias.html"

# def editar_noticia(request, noticia_id):
#     noticia = get_object_or_404(Noticia, pk=noticia_id)

#     if request.method == 'POST':
#         form = NoticiaForm(request.POST, instance=noticia)
#         if form.is_valid():
#             form.save()
#             return redirect('hola')
#     else:
#         form = NoticiaForm(instance=noticia)

#     return render(request, 'noticias/editar_noticia.html', {'form': form})

class editar_noticia(UpdateView):
    model = Noticia
    form_class = Form_Modificacion
    template_name = 'noticias/editar_noticia.html'
    #success_url = reverse_lazy('noticias:lista_noticias')
    def get_success_url(self):
        return reverse_lazy('noticias:detalle_noticia',kwargs={'noticia_id': self.object.pk})

def noticiasDestacadas(request):
    noticias = Noticia.objects.order_by('-fecha_publicacion')[:5]
    return render(request, 'noticias/noticias_destacadas.html', {'noticias': noticias})

def eliminar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)

    if request.method == 'POST':
        noticia.delete()
        return redirect('lista_noticias')

    return render(request, 'noticias/eliminar_noticia.html', {'noticia': noticia})

def detalleNoticia(request, noticia_id):
    ctx={}
    noticia = Noticia.objects.get(id=noticia_id)
    ctx['noticia']=noticia
    
    return render(request, 'noticias/detalle_noticia.html', ctx)

def FiltroCategoria(request, categoria_id):
    ctx={}
    categoria = Categoria.objects.get(id=categoria_id)
    filtrados = Noticia.objects.filter(categoria=categoria)
    
    return render(request, 'noticias/listar_noticias.html', {"noticias": filtrados})