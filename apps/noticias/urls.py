
from django.urls import path
from . import views

app_name="noticias"

urlpatterns = [
    path("catalogo", views.catalogo, name="catalogo"),
    path('crear_noticia', views.crear_noticia, name='crear_noticia'),
    path('listar_noticias', views.lista_noticias, name='lista_noticias'),
    path('editar_noticia/<int:noticia_id>/', views.editar_noticia, name='editar_noticia'),
    path('eliminar_noticia/<int:noticia_id>/', views.eliminar_noticia, name='eliminar_noticia')
]
