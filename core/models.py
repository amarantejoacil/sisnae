from django.db import models
from stdimage.models import StdImageField
from django.contrib.auth import get_user_model


class Base(models.Model):
    IncPor = models.IntegerField('Incluido Por', null=True, blank=True)
    AltPor = models.IntegerField('Alterado Por', null=True, blank=True)
    IncEm = models.DateTimeField('Incluido Em', auto_now_add=True)
    AltEm = models.DateTimeField('Alterado Em', auto_now=True)

    class Meta:
        abstract = True


class Pessoa(Base):
    nome = models.CharField('Nome', max_length=150)
    SEXO_CHOICES = (
        ('F', "Feminino"),
        ('M', "Masculino"),
        ('P', "Prefiro não informar"),
    )
    genero = models.CharField('Sexo', choices=SEXO_CHOICES, max_length=1)
    cpf = models.CharField('CPF', max_length=11)
    rg = models.CharField('RG', max_length=15)
    data_nascimento = models.DateField('Data de nascimento', null=True)
    foto = StdImageField('Image', upload_to='pessoa', variations={'thumb': {'width': 200, 'height': 200, 'crop': True}},
                         null=True, blank=True)
    email = models.EmailField('E-mail', max_length=200)
    cep = models.CharField('CEP', max_length=15)
    endereco = models.CharField('Endereço', max_length=100)
    numero = models.PositiveIntegerField('Número')
    bairro = models.CharField('Bairro', max_length=50)
    tel_celular = models.CharField('Nº do Celular', max_length=15)
    tel_telefone = models.CharField('N° de Telefone', max_length=15, null=True, blank=True)
    tel_responsavel = models.CharField('Nº do Reponsável', max_length=15)
    cidade = models.ForeignKey("Cidade", on_delete=models.RESTRICT, null=True)
    possui_conta = models.BooleanField('Possui conta?', default=True)
    TIPO_CONTA_CHOICES = (
        ('CP', "Conta Poupança"),
        ('CC', "Conta Corrente"),
        ('PP', "Conta Poupex"),
        ('PO', "Conta Poupança Ouro"),
        ('CU', "Conta Universitária"),
        ('CL', "Conta Salário"),
    )
    tipo_conta = models.CharField('Tipo de conta', choices=TIPO_CONTA_CHOICES, max_length=2)
    banco = models.ForeignKey("Banco", on_delete=models.RESTRICT, null= True)
    agencia = models.CharField('N° da Agência', max_length=20)
    conta = models.CharField('N° da Conta', max_length=20)

    ESCOLARIDADE_CHOICES = (
        (1, "Ensino Fundamental Incompleto"),
        (2, "Ensino Fundamental Completo"),
        (3, "Ensino Médio Incompleto"),
        (4, "Ensino Médio Completo"),
        (5, "Ensino Superior Incompleto"),
        (6, "Ensino Superior Completo"),
        (7, "Pós-Graduação"),
        (8, "Mestrado"),
        (9, "Doutorado"),
    )

    nome_pai = models.CharField('Nome do Pai', max_length=100, null=True, blank=True)
    escolaridade_pai = models.IntegerField('Escolaridade do Pai', choices=ESCOLARIDADE_CHOICES)
    nome_mae = models.CharField('Nome da Mãe', max_length=100)
    escolaridade_mae = models.IntegerField('Escolaridade da Mãe', choices=ESCOLARIDADE_CHOICES)








    pessoa_status = models.BooleanField('Pessoa ativa?', default=True)


    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    def __str__(self):
        return self.nome


class Cidade(Base):
    descricao = models.CharField('Descrição', max_length=100)
    cidade_status = models.BooleanField('Cidade ativa?', default=True)

    def __str__(self):
        return self.descricao


class Banco(Base):
    descricao = models.CharField('Descrição', max_length=100)
    banco_status = models.BooleanField('Banco ativo?', default=True)

    def __str__(self):
        return self.descricao
