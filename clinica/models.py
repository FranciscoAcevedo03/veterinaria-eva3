from django.db import models

class Especie(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name="Especie")
    descripcion = models.CharField(max_length=150, blank=True, verbose_name="Descripción")

    class Meta:
        verbose_name = "Especie"
        verbose_name_plural = "Especies"

    def __str__(self):
        return self.nombre


class Paciente(models.Model):
    especie = models.ForeignKey(
        Especie,
        on_delete=models.CASCADE,
        related_name='pacientes',
        verbose_name="Especie"
    )
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la Mascota")
    tutor = models.CharField(max_length=100, verbose_name="Nombre del Tutor")
    peso_kg = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Peso (kg)")
    fecha_ingreso = models.DateField(verbose_name="Fecha de Ingreso")
    vacunado = models.BooleanField(default=False, verbose_name="Vacunas al día")

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __str__(self):
        return f"{self.nombre} ({self.especie.nombre})"