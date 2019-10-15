from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from apps.core import views
from apps.funcionario.api.views import FuncionarioViewSet
from apps.registro_hora_extra.api.views import RegistroHoraExtraViewSet

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'funcionarios', FuncionarioViewSet)
router.register(r'horas-extras', RegistroHoraExtraViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include('apps.core.urls')),
    path('funcionario/', include('apps.funcionario.urls')),
    path('documento/', include('apps.documento.urls')),
    path('departamento/', include('apps.departamento.urls')),
    path('horaextra/', include('apps.registro_hora_extra.urls')),
    path('empresa/', include('apps.empresa.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
