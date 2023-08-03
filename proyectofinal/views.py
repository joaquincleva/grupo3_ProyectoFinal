from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages


def Hola(request):
    return render(request, "inicio.html")


def Acercade(request):
    return render(request, "sobre_nosotros.html")


def Contacto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        asunto = request.POST.get("asunto")
        tipo_consulta = request.POST.get("tipo_consulta")
        mensaje = request.POST.get("mensaje")

        # Enviar correo electrónico
        subject = f"Nuevo mensaje de contacto - {asunto}"
        message = f"Nombre: {nombre}\nTipo de consulta: {tipo_consulta}\nMensaje: {mensaje}"
        from_email = "grupoinformatorio@gmail.com"
        recipient_list = ["grupoinformatorio@gmail.com"]
        send_mail(subject, message, from_email, recipient_list)
        messages.success(request, "El correo ha sido enviado correctamente.")

        return render(request, "contacto.html")

    return render(request, "contacto.html")


def RutaConDatos(request):
    nombres = ["Pedro", "Pica", "Piedra"]
    booleanoVerdadero = True
    booleanoFalso = False
    return render(
        request,
        "rutaConDatos.html",
        {
            "nombres": nombres,
            "booleanoVerdadero": booleanoVerdadero,
            "booleanoFalso": booleanoFalso,
        },
    )
