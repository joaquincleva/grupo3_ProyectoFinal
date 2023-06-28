from django.shortcuts import render

def Home(request):
    return render(request,"inicio.html")

def Hola(request):
    return render(request,"hola.html")