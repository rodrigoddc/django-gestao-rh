from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from datetime import datetime
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