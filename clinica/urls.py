from django.urls import path
from .views import (
    PacienteListView,
    PacienteDetailView,
    PacienteCreateView,
    PacienteUpdateView,
    PacienteDeleteView,
)

urlpatterns = [
    path('', PacienteListView.as_view(), name='paciente_list'),
    path('paciente/<int:pk>/', PacienteDetailView.as_view(), name='paciente_detail'),
    path('nuevo/', PacienteCreateView.as_view(), name='paciente_create'),
    path('editar/<int:pk>/', PacienteUpdateView.as_view(), name='paciente_update'),
    path('eliminar/<int:pk>/', PacienteDeleteView.as_view(), name='paciente_delete'),
]