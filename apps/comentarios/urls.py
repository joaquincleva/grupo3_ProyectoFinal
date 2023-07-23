
from django.urls import path
from . import views 

app_name="comentarios"

urlpatterns = [
    path('agregar/<int:noticia_id>/', views.agregarComentario, name='agregar'),
    path('eliminar_comentario/<int:pk>/', views.BorrarComentario.as_view(), name='eliminar_comentario'),
    path('editar_comentario/<int:pk>/', views.editar_comentario.as_view(), name='editar_comentario'),

]