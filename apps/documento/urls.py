from django.urls import path
from .views import DocumentoCreate, DocumentoDelete

app_name = 'documento'
urlpatterns = [
    path('novo/', DocumentoCreate.as_view(), name='salvar'),
    path('deletar/<int:pk>/', DocumentoDelete.as_view(), name='delete'),
]