from django.urls import reverse_lazy
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


class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'clinica/paciente_form.html'
    success_url = reverse_lazy('paciente_list')


class PacienteUpdateView(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'clinica/paciente_form.html'
    success_url = reverse_lazy('paciente_list')


class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'clinica/paciente_confirm_delete.html'
    success_url = reverse_lazy('paciente_list')