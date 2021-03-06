# Generated by Django 3.2.6 on 2021-09-08 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0002_auto_20210907_2135'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionarioAnexo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IncPor', models.IntegerField(blank=True, null=True, verbose_name='Incluido Por')),
                ('AltPor', models.IntegerField(blank=True, null=True, verbose_name='Alterado Por')),
                ('IncEm', models.DateTimeField(auto_now_add=True, verbose_name='Incluido Em')),
                ('AltEm', models.DateTimeField(auto_now=True, verbose_name='Alterado Em')),
                ('quest_aluno_anexo_tipo', models.IntegerField(choices=[(1, 'Valor Gasto com Van'), (2, 'Valor Gasto com Aluguel ou Financiamento do Imovel'), (3, 'Valor Gasto com Energia'), (4, 'Valor Gasto com Água'), (5, 'Valor Gasto com Conomínio'), (6, 'Valor Gasto com Medicação')], verbose_name='Inclua os anexos das suas despesas')),
                ('quest_aluno_anexo_valor', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Informe o valor do anexo')),
                ('quest_aluno_anexo_arq', models.CharField(max_length=100, verbose_name='Anexo/Comprovante')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
