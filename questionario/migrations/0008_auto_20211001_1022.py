# Generated by Django 3.2.6 on 2021-10-01 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0007_remove_questionario_aluno'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionario',
            name='questionario_ano',
            field=models.IntegerField(default=2021, verbose_name='Ano do questionário:'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionario',
            name='questionario_semestre',
            field=models.IntegerField(choices=[(1, '1° Semestre'), (2, '2° Semestre')], default=1, verbose_name='Semestre'),
            preserve_default=False,
        ),
    ]
