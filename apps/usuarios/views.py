from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegistroForm
# Create your views here.

class Registro(CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy("login")
    template_name="usuarios/registrar.html"