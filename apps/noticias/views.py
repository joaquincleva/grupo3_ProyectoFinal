from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404, redirect
from django.db.models import Q
from .forms import Form_Modificacion, Form_Alta
from .models import Noticia,Categoria
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins    import UserPassesTestMixin
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def catalogo(request):
    return render(request, 'noticias/catalogo.html')

class crear_noticia(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Noticia
    form_class=Form_Alta
    template_name="noticias/crear_noticia.html"
    success_url=reverse_lazy("noticias:lista_noticias")

    def test_func(self):
        return self.request.user.is_staff
    
    def form_valid(self, form):
        noti=form.save(commit=False)
        noti.autor=self.request.user
        return super(crear_noticia,self).form_valid(form)


def lista_noticias(request):
    ctx = {}
    categorias = Categoria.objects.all()
    filtro = request.GET.get('fl', None)
    orden = request.GET.get('orden', None)
    query = request.GET.get('q', None)

    if filtro:
        if filtro == 'todas':
            todas_noticias = Noticia.objects.all()
        else:
            cat_filtro = Categoria.objects.filter(nombre=filtro)
            if cat_filtro:
                todas_noticias = Noticia.objects.filter(categoria=cat_filtro[0])
            else:
                todas_noticias = []
                ctx['error'] = "No existe la categoria ingresada."
    else:
        todas_noticias = Noticia.objects.all()

    if query:
        todas_noticias = todas_noticias.filter(Q(titulo__icontains=query) | Q(contenido__icontains=query))

    if orden:
        if orden == 'ala':
            todas_noticias = todas_noticias.order_by('titulo')
        elif orden == 'ald':
            todas_noticias = todas_noticias.order_by('-titulo')
        elif orden == 'ana':
            todas_noticias = todas_noticias.order_by('fecha_publicacion')
        elif orden == 'and':
            todas_noticias = todas_noticias.order_by('-fecha_publicacion')

    ctx['object_list'] = todas_noticias
    ctx['categorias'] = categorias

    return render(request, 'noticias/listar_noticias.html', {'noticias': todas_noticias})

class Categorias(ListView):
    model = Categoria
    template_name = "noticias/listar_categorias.html"

class editar_noticia(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Noticia
    form_class = Form_Modificacion
    template_name = 'noticias/editar_noticia.html'
    def get_success_url(self):
        return reverse_lazy('noticias:detalle_noticia',kwargs={'noticia_id': self.object.pk})

    def test_func(self):
        return self.request.user.is_staff

def noticiasDestacadas(request):
    noticias = Noticia.objects.order_by('-fecha_publicacion')[:8]
    return render(request, 'noticias/noticias_destacadas.html', {'noticias': noticias})

@staff_member_required
def eliminar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)

    if request.method == 'POST':
        noticia.delete()
        return redirect('noticias:lista_noticias')

    return render(request, 'noticias/eliminar_noticia.html', {'noticia': noticia})

def detalleNoticia(request, noticia_id):
    ctx={}
    noticia = Noticia.objects.get(id=noticia_id)
    ctx['noticia']=noticia
    
    return render(request, 'noticias/detalle_noticia.html', ctx)

def noticiasImagenes(request):
    todas_noticias = Noticia.objects.all()
    return render(request, 'noticias/noticias_imagenes.html', {'object_list': todas_noticias})

def FiltroCategoria(request, categoria_id):
    ctx={}
    categoria = Categoria.objects.get(id=categoria_id)
    filtrados = Noticia.objects.filter(categoria=categoria)
    
    return render(request, 'noticias/listar_noticias.html', {"noticias": filtrados})