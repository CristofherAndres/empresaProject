from django import forms
from empleadosApp.models import Persona, Estado
#Libreria para realizar validaciones de datos manuales
from django.core import validators

""" Actualizar """
class PersonaForm(forms.Form):
    nombre      = forms.CharField(validators=[
                    validators.MaxLengthValidator(50),
                    validators.MinLengthValidator(2)
    ])
    apellido    = forms.CharField()
    telefono    = forms.CharField()
    email       = forms.EmailField()
    estado      = forms.ModelChoiceField(queryset=Estado.objects.all())

    nombre.widget.attrs['class'] = 'form-control'
    apellido.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-control'


""" Insertar """
class PersonaForm(forms.ModelForm):
    nombre      = forms.CharField(validators=[
                    validators.MaxLengthValidator(50),
                    validators.MinLengthValidator(2)
    ])
    apellido    = forms.CharField()
    telefono    = forms.CharField()
    email       = forms.EmailField()
    estado      = forms.ModelChoiceField(queryset=Estado.objects.all())

    nombre.widget.attrs['class'] = 'form-control'
    apellido.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Persona
        fields = '__all__'
