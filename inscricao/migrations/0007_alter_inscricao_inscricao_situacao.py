# Generated by Django 3.2.6 on 2021-10-19 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscricao', '0006_auto_20211017_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscricao',
            name='inscricao_situacao',
            field=models.IntegerField(choices=[(1, 'Inscrição realizada'), (2, 'Realizar Correção'), (3, 'Inscrição Deferida'), (4, 'Inscrição Indeferida'), (5, 'Inscrição Cancelada')], default=1),
        ),
    ]
