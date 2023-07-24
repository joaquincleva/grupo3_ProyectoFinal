from django.shortcuts import render

def Hola(request):
    return render(request,"inicio.html")

def PruebaTemplate(request):
    return render(request,"pruebaTemplate.html")

def RutaConDatos(request):
    nombres = ["Pedro","Pica","Piedra"]
    booleanoVerdadero=True
    booleanoFalso=False
    return render(request, "rutaConDatos.html",{"nombres":nombres, "booleanoVerdadero":booleanoVerdadero, "booleanoFalso":booleanoFalso})