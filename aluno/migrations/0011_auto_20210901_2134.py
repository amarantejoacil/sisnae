# Generated by Django 3.2.6 on 2021-09-02 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0010_auto_20210901_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='aluno_nome_pai_asdasda_sadasdasdas_asudhaudhuashdusa',
        ),
        migrations.AddField(
            model_name='aluno',
            name='aluno_nome_pai',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]