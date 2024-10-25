from django.shortcuts import render
#Importar el modelo persona
from empleadosApp.models import Persona
from empleadosApp.forms import PersonaForm

""" Importar para redirigir """
from django.urls import reverse
from django.http import HttpResponseRedirect

""" Decorador para exigir el uso del logeo """
from django.contrib.auth.decorators import login_required

""" Registro de usuario """
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

# Create your views here.

@login_required
def listaPersonas(request):
    #Select * from empleados
    personas = Persona.objects.all()
    data = {'personas': personas}
    return render(request, 'empleadosApp/personas.html', data)

@login_required
def agregarPersonas(request):
    form = PersonaForm() # Inicia la pagina con un formulario vacio
    
    if request.method == 'POST': #Cuando lleno el formulario y apreto enviar
        form = PersonaForm(request.POST) #Se rescatan los datos del formulario
        if form.is_valid():
            print("El formulario es valido")
            form.save()
            return HttpResponseRedirect(reverse('listaPersonas'))
    
    data = {'form': form,
            'titulo':'Agregar Persona',
            'boton' : 'Registrar'
            }
    return render(request, 'empleadosApp/personaForm.html', data)

@login_required
def eliminarPersona(request, id):
    """ Buscar a la persona a eliminar por id """
    persona = Persona.objects.get(id = id)
    persona.delete()
    return HttpResponseRedirect(reverse('listaPersonas'))

@login_required
def editarPersona(request, id):
    """ Recuperar los datos de la persona según su id """
    persona = Persona.objects.get(id = id)
    """ Le paso los datos de la persona al form """
    form = PersonaForm(instance=persona) # Inicia la pagina con un formulario vacio
    
    if request.method == 'POST': #Cuando lleno el formulario y apreto enviar
        form = PersonaForm(request.POST, instance=persona) #Se rescatan los datos del formulario
        if form.is_valid():
            print("El formulario es valido")
            form.save()
            return HttpResponseRedirect(reverse('listaPersonas'))
    
    data = {'form': form,
            'titulo': 'Editar Persona',
            'boton' : 'Editar'}
    return render(request, 'empleadosApp/personaForm.html', data)


