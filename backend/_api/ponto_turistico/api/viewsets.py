from rest_framework.viewsets import ModelViewSet
from ponto_turistico.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.decorators import action

class PontoTuristicoViewSet(ModelViewSet):
    #queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
# query string é a terceira forma de fazer a filtragem
# exemplo de aplicação
# endereço http:
# localhost:8000/pontosturisticos/?id=8&nome=ponto 008&descricao=teste
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()
        if id:
            queryset = PontoTuristico.objects.filter(pk = id)

        if nome:
            queryset = queryset.filter(nome__iexact = nome)

        if descricao:
            queryset = queryset.filter(descricao__iexact = descricao)

        return queryset
        # return PontoTuristico.objects.filter(aprovado = True)  # primeira forma de filtrar
        # DJANGO FILTER é a quarta forma de filtrar
        # https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend
        # SEARCH FILTER é a quinta forma de filtrar (busca uma informação por um critério OU por outro OU por outro...)
        # vídeo 27
        # https://www.django-rest-framework.org/api-guide/filtering/#searchfilter


    def list(self, request, *args, **kwargs):  # segunda forma de filtrar (faz a filtragem dentro da função)
        #pass
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    @action(methods = ['get', 'post'], detail = True)
    def denunciar(self, request, pk=None):
        pass
