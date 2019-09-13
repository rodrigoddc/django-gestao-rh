from django.urls import path, include
from .views import EmpresaCreate, EmpresaEdit

app_name = 'empresa'
urlpatterns = [
    path('criar/', EmpresaCreate.as_view(), name='criar'),
    path('editar/<int:pk>/', EmpresaEdit.as_view(), name='editar'),
]
