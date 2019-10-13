from django.urls import path
from .views import (HoraExtraList,
                    HoraExtraCreate,
                    HoraExtraFuncionarioCreate,
                    HoraExtraUpdate,
                    HoraExtraFuncionarioUpdate,
                    HoraExtraDelete,
                    UtilizouHoraExtra)
from .views import ExportarCSV


app_name = 'horaextra'
urlpatterns = [
    path('listar/', HoraExtraList.as_view(), name='listar'),
    path('criar/', HoraExtraCreate.as_view(), name='criar'),
    path('criar-por-funcionario/<int:funcionario_pk>/', HoraExtraFuncionarioCreate.as_view(), name='criar-por-funcionario'),
    path('atualizar/<int:pk>/', HoraExtraUpdate.as_view(), name='atualizar'),
    path('utilizouhoraextra/<int:pk>/', UtilizouHoraExtra.as_view(), name='utilizouhoraextra'),
    path('atualizar-por-funcionario/<int:pk>/', HoraExtraFuncionarioUpdate.as_view(), name='atualizar-por-funcionario'),
    path('deletar/<int:pk>/', HoraExtraDelete.as_view(), name='deletar'),
    path('exportar_csv', ExportarCSV.as_view(), name='exportar_csv'),
]


