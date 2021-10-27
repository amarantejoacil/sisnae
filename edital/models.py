from core.models import Base
from django.db import models


class Edital(Base):
    edital_descricao = models.CharField('Descrição', max_length=200)
    edital_titulo = models.CharField('Título', max_length=200)
    numero = models.PositiveIntegerField('Nº do Edital')
    SEMESTRE = (
        (1, "1° Semestre"),
        (2, "2° Semestre"),
    )
    semestre_edital = models.IntegerField('Semestre', choices=SEMESTRE)
    ano = models.PositiveIntegerField('Ano')
    edital_datetime_ini = models.DateTimeField('Edital Aberto em Inicio:',null=True, blank=True)
    edital_datetime_fim = models.DateTimeField('Edital Fechado em:', null=True, blank=True)
    edital_datetime_correcao_ini = models.DateTimeField('Data Inicio para correção', null=True, blank=True)
    edital_datetime_correcao_fim = models.DateTimeField('Data Final para correção', null=True, blank=True)
    edital_status = models.BooleanField('Edital ativo?', default=True)
    modalidade_edital = models.ForeignKey("ModalidadeEdital", on_delete=models.RESTRICT)
    setor = models.ForeignKey("SetorEdital", on_delete=models.RESTRICT)
    edital_quantidade_vaga = models.IntegerField('Quantidade de vaga')
    edital_valor_auxilio = models.DecimalField('Valor do auxílio', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Edital'
        verbose_name_plural = 'Editais'

    def __str__(self):
        return 'Edital: N° ' + str(self.numero) + '/' \
               + str(self.ano) + ' | ' + str(self.edital_titulo)


class PublicacaoEdital(Base):
    edital = models.ForeignKey("Edital", on_delete=models.RESTRICT)
    publicacao_descricao = models.CharField('Descrição', max_length=150)
    publicacao_anexo_arq = models.FileField('Publicação arquivo', upload_to='media/publicacao')
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
