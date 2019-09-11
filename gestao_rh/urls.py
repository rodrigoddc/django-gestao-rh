from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.core.urls')),
    path('funcionario/', include('apps.funcionario.urls')),
    path('departamento/', include('apps.departamento.urls')),
    path('empresa/', include('apps.empresa.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
