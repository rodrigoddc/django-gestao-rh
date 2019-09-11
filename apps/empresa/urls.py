from django.urls import path, include
from .views import EmpresaCreate, EmpresaEdit

app_name = 'empresa'
urlpatterns = [
    path('novo/', EmpresaCreate.as_view(), name='empresa_criar'),
    path('editar/<int:pk>/', EmpresaEdit.as_view(), name='empresa_editar'),
]
