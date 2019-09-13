from django.urls import path
from .views import (HoraExtraList,
                    HoraExtraCreate,
                    HoraExtraUpdate,
                    HoraExtraDelete)

app_name = 'horaextra'
urlpatterns = [
    path('listar/', HoraExtraList.as_view(), name='listar'),
    path('criar/', HoraExtraCreate.as_view(), name='criar'),
    path('atualizar/<int:pk>/', HoraExtraUpdate.as_view(), name='atualizar'),
    path('deletar/<int:pk>/', HoraExtraDelete.as_view(), name='deletar'),
]


