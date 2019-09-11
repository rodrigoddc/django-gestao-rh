from django.shortcuts import render
from django.views.generic import CreateView, DeleteView

from apps.documento.models import Documento


class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']
    success_url = 'core:home'


class DocumentoDelete(DeleteView):
    model = Documento
    success_url = 'core:home'