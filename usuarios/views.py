from django.shortcuts import render,redirect
from .models import persona
from .formulario import PersonaFormulario

# Create your views here.

def listar_personas(request):
    personas=persona.objects.all()
    return render (request,'listar_personas.html',{'personas':personas})

def crear_persona(request):
    if request.method =='POST':
        form= PersonaFormulario(request.POST)
        if form.is_valid:
            form.save()
            return redirect(listar_personas)
    else:
        form =PersonaFormulario()
        return render(request,'crear_persona.html',{'form':form})
