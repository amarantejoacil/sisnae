# Generated by Django 3.2.6 on 2021-08-31 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_aluno_pessoa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IncPor', models.IntegerField(blank=True, null=True, verbose_name='Incluido Por')),
                ('AltPor', models.IntegerField(blank=True, null=True, verbose_name='Alterado Por')),
                ('IncEm', models.DateTimeField(auto_now_add=True, verbose_name='Incluido Em')),
                ('AltEm', models.DateTimeField(auto_now=True, verbose_name='Alterado Em')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('banco_status', models.BooleanField(default=True, verbose_name='Banco ativo?')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='aluno',
            old_name='status_aluno',
            new_name='aluno_status',
        ),
        migrations.RenameField(
            model_name='cidade',
            old_name='status_cidade',
            new_name='cidade_status',
        ),
        migrations.RenameField(
            model_name='pessoa',
            old_name='status_pessoa',
            new_name='pessoa_status',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='banco',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='core.banco'),
        ),
    ]
