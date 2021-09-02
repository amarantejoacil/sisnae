# Generated by Django 3.2.6 on 2021-09-02 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0018_auto_20210902_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='aluno_lactante',
            field=models.BooleanField(default=False, verbose_name='Você é Lactante? '),
        ),
        migrations.AddField(
            model_name='aluno',
            name='aluno_medicacao',
            field=models.BooleanField(default=False, verbose_name='Medicamentos de Uso Regular?'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='aluno_gestante',
            field=models.BooleanField(default=False, verbose_name='Aluna está Gestante? '),
        ),
    ]
