from django.contrib import admin
from .models import Especie, Paciente

@admin.register(Especie)
class EspecieAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)
    list_filter = ('nombre',)

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'especie', 'tutor', 'peso_kg', 'fecha_ingreso', 'vacunado')
    list_filter = ('especie', 'vacunado', 'fecha_ingreso')
    search_fields = ('nombre', 'tutor')