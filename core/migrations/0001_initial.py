# Generated by Django 3.2.6 on 2021-08-27 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IncPor', models.IntegerField(blank=True, null=True, verbose_name='Incluido Por')),
                ('AltPor', models.IntegerField(blank=True, null=True, verbose_name='Alterado Por')),
                ('IncEm', models.DateTimeField(auto_now_add=True, verbose_name='Incluido Em')),
                ('AltEm', models.DateTimeField(auto_now=True, verbose_name='Alterado Em')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.pessoa')),
                ('matricula', models.IntegerField(unique=True, verbose_name='Matricula')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.pessoa',),
        ),
    ]
