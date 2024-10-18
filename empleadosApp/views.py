from django.shortcuts import render
#Importar el modelo persona
from empleadosApp.models import Persona
from empleadosApp.forms import PersonaForm

""" Importar para redirigir """
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

def listaPersonas(request):
    #Select * from empleados
    personas = Persona.objects.all()
    data = {'personas': personas}
    return render(request, 'empleadosApp/personas.html', data)

def agregarPersonas(request):
    form = PersonaForm() # Inicia la pagina con un formulario vacio
    
    if request.method == 'POST': #Cuando lleno el formulario y apreto enviar
        form = PersonaForm(request.POST) #Se rescatan los datos del formulario
        if form.is_valid():
            print("El formulario es valido")
            form.save()
            return HttpResponseRedirect(reverse('listaPersonas'))
    
    data = {'form': form}
    return render(request, 'empleadosApp/personaForm.html', data)

def eliminarPersona(request, id):
    """ Buscar a la persona a eliminar por id """
    persona = Persona.objects.get(id = id)
    persona.delete()
    return HttpResponseRedirect(reverse('listaPersonas'))

