from django.db import models
from apps.funcionario.models import Funcionario


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100, verbose_name='Registro de Hora Extra')
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    def __str__(self):
        return self.motivo
