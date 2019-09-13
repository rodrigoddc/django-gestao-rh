from django.db import models
from django.urls import reverse
from apps.funcionario.models import Funcionario


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100, verbose_name='Registro de Hora Extra')
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    horas = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.motivo
