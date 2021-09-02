from core.models import Base
from django.db import models


class Edital(Base):
    titulo = models.CharField('Título do Edital', max_length=200)
    descricao = models.CharField('Descrição', max_length=200)
    numero = models.PositiveIntegerField('Nº do Edital')
    ano = models.PositiveIntegerField('Informe o ano do Edital')
    data_hora_inicio = models.DateTimeField('Validade Data/Hora Inicio:', null=True)
    data_hora_fim = models.DateTimeField('Validade Data/Hora Inicio:', null=True)
    edital_status = models.BooleanField('Edital ativo?', default=True)
    modalidade_edital = models.ForeignKey("ModalidadeEdital", on_delete=models.RESTRICT)
    setor = models.ForeignKey("SetorEdital", on_delete=models.RESTRICT)

    class Meta:
        verbose_name = 'Edital'
        verbose_name_plural = 'Editais'

    def __str__(self):
        return self.descricao


class PublicacaoEdital(Base):
    edital = models.ForeignKey("Edital", on_delete=models.RESTRICT)
    publicacao_descricao = models.CharField('Descrição', max_length=150)
    publicacao_anexo_arq = models.CharField(max_length=100)
    publicacao_data = models.DateField('Data da publicação', null=True, blank=True)

    def __str__(self):
        return self.publicacao_descricao

    class Meta:
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'

class ModalidadeEdital(Base):
    modalidade_desc = models.CharField('Descricao', max_length=100)
    modalidade_status = models.BooleanField('Modalidade ativa?', default=True)

    def __str__(self):
        return self.modalidade_desc

    class Meta:
        verbose_name = 'Modalidade'
        verbose_name_plural = 'Modalidades'


class SetorEdital(Base):
    setor_descricao = models.CharField('Nome do Setor', max_length=200)
    setor_siglas = models.CharField('Sigla do Setor', max_length=20)
    setor_status = models.BooleanField('Ativo?', default=True)

    def __str__(self):
        return self.setor_descricao

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'
