from django.db import models
from django.db.models import Sum
from django.urls import reverse
from django.contrib.auth.models import User
from apps.departamento.models import Departamento
from apps.empresa.models import Empresa


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamento = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('funcionario:listar')

    @property
    def total_hora_extra(self):

        if self.registrohoraextra_set.filter(utilizada=False) != 0:
            total = self.registrohoraextra_set.filter(utilizada=False).aggregate(Sum('horas'))['horas__sum']
            return total
        else:
            return 0

    def __str__(self):
        return self.nome