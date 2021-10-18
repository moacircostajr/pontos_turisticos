from rest_framework.serializers import ModelSerializer
from ponto_turistico.models import PontoTuristico

class PontoTuristicoSerializer(ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ['id', 'nome', 'descricao', 'foto']

class PontoTuristicoFullSerializer(ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ['id', 'nome', 'descricao', 'aprovado', 'atracao', 'comentarios', 'avaliacoes', 'endereco', 'foto']
