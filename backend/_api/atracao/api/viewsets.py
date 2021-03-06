from rest_framework.viewsets import ModelViewSet
from atracao.models import Atracao
from .serializers import AtracaoSerializer

class AtracaoViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    #permission_classes = [permissions.IsAuthenticated]