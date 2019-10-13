from django.urls import path

from .views import (FuncionarioList,
                    FuncionarioUpdate,
                    FuncionarioDelete,
                    FuncionarioCreate)
from .views import pdf_reportlab


app_name = 'funcionario'
urlpatterns = [
    path('listar/', FuncionarioList.as_view(), name='listar'),
    path('criar/', FuncionarioCreate.as_view(), name='criar'),
    path('atualizar/<int:pk>/', FuncionarioUpdate.as_view(), name='atualizar'),
    path('deletar/<int:pk>/', FuncionarioDelete.as_view(), name='deletar'),
    path('pdf-reportlab', pdf_reportlab, name='pdf_reportlab'),
]
