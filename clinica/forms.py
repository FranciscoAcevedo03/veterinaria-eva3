from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['especie', 'nombre', 'tutor', 'peso_kg', 'fecha_ingreso', 'vacunado']
        widgets = {
            'especie': forms.Select(attrs={'class': 'form-select'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Firulais'}),
            'tutor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Juan Pérez'}),
            'peso_kg': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'vacunado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }