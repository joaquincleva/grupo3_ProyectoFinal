from django.shortcuts import render,get_object_or_404, redirect
from .forms import NoticiaForm
from .models import Noticia 

# Create your views here.
def catalogo(request):
    return render(request, 'noticias/catalogo.html')

def crear_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hola')
    else:
        form = NoticiaForm()
    return render(request, 'noticias/crear_noticia.html', {'form': form})

def lista_noticias(request):
    noticias = Noticia.objects.order_by('-fecha_publicacion')
    return render(request, 'noticias/listar_noticias.html', {'noticias': noticias})

def editar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)

    if request.method == 'POST':
        form = NoticiaForm(request.POST, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('hola')
    else:
        form = NoticiaForm(instance=noticia)

    return render(request, 'noticias/editar_noticia.html', {'form': form})


def eliminar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)

    if request.method == 'POST':
        noticia.delete()
        return redirect('lista_noticias')

    return render(request, 'noticias/eliminar_noticia.html', {'noticia': noticia})