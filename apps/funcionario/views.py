import io
from django.contrib.auth.models import User
from django.http import HttpResponse, FileResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from datetime import datetime

from reportlab.pdfgen import canvas

from .models import Funcionario


class FuncionarioList(ListView):
    model = Funcionario

    def get_queryset(self):

        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome', 'departamento']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        funcionario.empresa = self.request.user.funcionario.empresa
        username = funcionario.nome + str(datetime.now().hour) + str(datetime.now().minute)
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioCreate, self).form_valid(form)


class FuncionarioUpdate(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamento']


class FuncionarioDelete(DeleteView):
    model = Funcionario

    success_url = reverse_lazy('funcionario:listar')


def pdf_reportlab(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'

    buffer = io.BytesIO()

    p = canvas.Canvas(buffer)

    p.drawString(10, 810, 'Relatorio Funcioanrio.')

    funcionarios = Funcionario.objects.filter(empresa=request.user.funcionario.empresa)

    str_ = 'Nome: %s  |  Horas extras %s'

    y = 790
    for funcionario in funcionarios:
        p.drawString(10, y, str_ % (funcionario.nome, funcionario.total_hora_extra))
        y -= 40

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response
