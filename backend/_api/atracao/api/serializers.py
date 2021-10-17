from rest_framework.serializers import ModelSerializer
from atracao.models import Atracao

class AtracaoSerializer(ModelSerializer):
    class Meta:
        model = Atracao
        fields = ['id', 'nome', 'descricao', 'horario_func', 'idade_minima']

class AtracaoFullSerializer(ModelSerializer):
    class Meta:
        model = Atracao
        fields = ['id', 'nome', 'descricao', 'horario_func', 'idade_minima']
