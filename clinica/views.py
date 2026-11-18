from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Paciente
from .forms import PacienteForm

class PacienteListView(ListView):
    model = Paciente
    template_name = 'clinica/paciente_list.html'
    context_object_name = 'pacientes'

    def get_queryset(self):
        return Paciente.objects.select_related('especie').all()


class PacienteDetailView(DetailView):
    model = Paciente
    template_name = 'clinica/paciente_detail.html'
    context_object_name = 'paciente'


class PacienteCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'clinica/paciente_form.html'
    success_url = reverse_lazy('paciente_list')
    success_message = "Paciente registrado exitosamente."


class PacienteUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'clinica/paciente_form.html'
    success_url = reverse_lazy('paciente_list')
    success_message = "Datos del paciente actualizados correctamente."


class PacienteDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Paciente
    template_name = 'clinica/paciente_confirm_delete.html'
    success_url = reverse_lazy('paciente_list')
    success_message = "Paciente eliminado del sistema."