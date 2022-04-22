from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Views here.

def inicio(request):
    return render(request, "inicio.html")





def exito(request):
    if request.method == "POST":
        asunto = request.POST["txtAsunto"]
        mensaje = request.POST["txtMensaje"] + " / Email: " + request.POST["txtEmail"]
        
        datos_del_formulario = [asunto, mensaje]
        
        
        return render(request, "exito.html")