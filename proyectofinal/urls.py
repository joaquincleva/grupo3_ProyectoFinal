"""proyectofinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.Hola, name="hola"),
    path("pruebatemplate", views.PruebaTemplate, name="pruebaTemplate"),#Si viene url "pruebatemplate" dsps de la barra de la 
                                            #url se ejecuta la función views
    path("rutacondatos", views.RutaConDatos, name="usuarios"),
    path("noticias/", include('apps.noticias.urls'), name="noticias"),
    path("comentarios/", include('apps.comentarios.urls'), name="comentarios"),

    path("login/", auth.LoginView.as_view(template_name="usuarios/login.html"), name="login"),
    path("logout/", auth.LogoutView.as_view(), name="logout"),
    
    path("usuarios/", include('apps.usuarios.urls'), name="usuarios"),


    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

