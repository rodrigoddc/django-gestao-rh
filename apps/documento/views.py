from django.shortcuts import render
from django.views.generic import CreateView, DeleteView

from apps.documento.models import Documento


class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.pertence_id = self.kwargs['funcionario_pk']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class DocumentoDelete(DeleteView):
    model = Documento
    success_url = 'core:home'