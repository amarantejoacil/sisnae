from django.db import models
from core.models import Base

class Inscricao(Base):
    situacao_obs = models.CharField('Observação da inscrição', max_length=200, null=True)
    nome = models.CharField('nome', max_length=100, null=True)