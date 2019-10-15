from rest_framework import serializers
from apps.funcionario.models import Funcionario
from apps.registro_hora_extra.api.serializers import RegistroHoraExtraSerializer


class FuncionarioSerializer(serializers.ModelSerializer):

    registrohoraextra_set = RegistroHoraExtraSerializer(many=True)

    class Meta:
        model = Funcionario
        fields = [
            'user',
            'nome',
            'empresa',
            'departamento',
            'total_hora_extra',
            'registrohoraextra_set'
        ]
