from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from apps.registro_hora_extra.api.serializers import RegistroHoraExtraSerializer
from apps.registro_hora_extra.models import RegistroHoraExtra


class RegistroHoraExtraViewSet(viewsets.ModelViewSet):
    queryset = RegistroHoraExtra.objects.all()
    serializer_class = RegistroHoraExtraSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

