# Generated by Django 3.2.6 on 2021-09-02 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('edital', '0001_initial'),
        ('aluno', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IncPor', models.IntegerField(blank=True, null=True, verbose_name='Incluido Por')),
                ('AltPor', models.IntegerField(blank=True, null=True, verbose_name='Alterado Por')),
                ('IncEm', models.DateTimeField(auto_now_add=True, verbose_name='Incluido Em')),
                ('AltEm', models.DateTimeField(auto_now=True, verbose_name='Alterado Em')),
                ('inscricao_situacao', models.IntegerField(choices=[(1, 'inscrição realizada'), (2, 'realizar correção'), (3, 'inscrição deferida'), (4, 'inscrição indeferida')], default=1)),
                ('situacao_obs', models.CharField(blank=True, max_length=200, null=True, verbose_name='Observação da inscrição')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aluno.aluno')),
                ('edital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edital.edital')),
            ],
            options={
                'verbose_name': 'Inscrição',
                'verbose_name_plural': 'Inscrições',
            },
        ),
    ]
