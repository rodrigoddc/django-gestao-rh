from django.urls import path
from .views import (DepartamentoList,
                    DepartamentoCreate,
                    DepartamentoUpdate,
                    DepartamentoDelete)

app_name = 'departamento'
urlpatterns = [
    path('listar/', DepartamentoList.as_view(), name='listar'),
    path('criar/', DepartamentoCreate.as_view(), name='criar'),
    path('atualizar/<int:pk>/', DepartamentoUpdate.as_view(), name='atualizar'),
    path('deletar/<int:pk>/', DepartamentoDelete.as_view(), name='deletar'),
]


