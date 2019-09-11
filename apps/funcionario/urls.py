from django.urls import path
from .views import (FuncionarioList,
                    FuncionarioUpdate,
                    FuncionarioDelete,
                    FuncionarioCreate)

app_name = 'funcionario'
urlpatterns = [
    path('listar/', FuncionarioList.as_view(), name='listar'),
    path('salvar/', FuncionarioCreate.as_view(), name='salvar'),
    path('atualizar/<int:pk>/', FuncionarioUpdate.as_view(), name='atualizar'),
    path('deletar/<int:pk>/', FuncionarioDelete.as_view(), name='deletar'),
]
