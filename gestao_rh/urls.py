from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('funcionario/', include('apps.funcionario.urls')),
    path('documento/', include('apps.documento.urls')),
    path('departamento/', include('apps.departamento.urls')),
    path('empresa/', include('apps.empresa.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
