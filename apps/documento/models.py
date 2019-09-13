from django.urls import reverse
from django.db import models
from apps.funcionario.models import Funcionario


class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    pertence = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to='documentos')

    def get_absolute_url(self):
        return reverse('funcionario:atualizar', args=[self.pertence.id])

    def __str__(self):
        return self.descricao
