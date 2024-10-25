from django.contrib import admin
from empleadosApp.models import Persona, Estado

# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','email','telefono']

admin.site.register(Persona, PersonaAdmin)
admin.site.register(Estado)
