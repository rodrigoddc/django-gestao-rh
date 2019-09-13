from django.urls import path
from .views import DocumentoCreate, DocumentoDelete
from apps.funcionario.models import Funcionario

app_name = 'documento'
urlpatterns = [
    path('criar/<int:funcionario_pk>', DocumentoCreate.as_view(), name='criar'),
    path('deletar/<int:pk>/', DocumentoDelete.as_view(), name='delete'),
]