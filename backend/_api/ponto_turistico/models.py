from django.db import models
from atracao.models import Atracao
from comentario.models import Comentario
from avaliacao.models import Avaliacao
from endereco.models import Endereco

# Create your models here.

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default = False)
    atracao = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(Endereco, on_delete = models.CASCADE, null = True)
    foto = models.ImageField(upload_to = 'pontos_turisticos', null = True, blank = True)

    def __str__(self):
        return self.nome
