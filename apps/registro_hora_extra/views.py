import csv
import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import UpdateView, DeleteView, CreateView, ListView
from .models import RegistroHoraExtra
from .forms import RegistroHoraExtraForm


class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class HoraExtraCreate(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm
    success_url = reverse_lazy('horaextra:listar')

    def get_form_kwargs(self):
        kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraFuncionarioCreate(CreateView):
    model = RegistroHoraExtra
    fields = ['motivo', 'horas']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.funcionario_id = self.kwargs['funcionario_pk']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('funcionario:atualizar', args=[self.object.funcionario.pk])


class HoraExtraUpdate(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraUpdate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_success_url(self):
        return reverse_lazy('horaextra:listar')


class HoraExtraFuncionarioUpdate(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraFuncionarioUpdate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_success_url(self):
        return reverse('funcionario:atualizar', args=[self.object.funcionario.pk])


class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('horaextra:listar')


class UtilizouHoraExtra(View):
    def post(self, *args, **kwargs):

        registro_hora_extra = RegistroHoraExtra.objects.get(id=kwargs['pk'])

        if self.request.POST['boolean'] == 'False':
            registro_hora_extra.utilizada = False
            mensagem = 'horas não utilizadas',
        else:
            mensagem = 'horas utilizadas',
            registro_hora_extra.utilizada = True

        registro_hora_extra.save()

        empregado = self.request.user.funcionario

        response = json.dumps({
            'mensagem': mensagem,
            'horas': round(float(empregado.total_hora_extra), 2)
        })

        return HttpResponse(response, content_type='application/json', status=200)


class ExportarCSV(View):

    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

        registro_horasextras = RegistroHoraExtra.objects.filter(utilizada=False)

        writer = csv.writer(response)
        writer.writerow([
            'Id',
            'Motivo',
            'Funcionario',
            'Rest. Funcionario',
            'Horas'])

        for registro in registro_horasextras:
            writer.writerow([
                registro.id,
                registro.motivo,
                registro.funcionario,
                registro.funcionario.total_hora_extra,
                registro.horas])

        return response