from django.db import models
from django.urls import reverse

from apps import empresa


class Empresa(models.Model):
    nome = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('empresa:editar', args=[self.pk])

    def __str__(self):
        return self.nome
