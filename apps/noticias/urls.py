
from django.urls import path
from . import views

app_name="noticias"

urlpatterns = [
    path("catalogo", views.catalogo, name="catalogo"),
    path('crear_noticia', views.crear_noticia.as_view(), name='crear_noticia'),
    path('listar_noticias', views.lista_noticias, name='lista_noticias'),
    path('editar_noticia/<int:pk>/', views.editar_noticia.as_view(), name='editar_noticia'),
    path('eliminar_noticia/<int:noticia_id>/', views.eliminar_noticia, name='eliminar_noticia'),
    path('detalle/<int:noticia_id>/', views.detalleNoticia, name='detalle_noticia'),
    path("categorias", views.Categorias.as_view(), name="categorias"),
    path("filtro_categoria/<int:categoria_id>/", views.FiltroCategoria, name="filtro_categoria"),
]
