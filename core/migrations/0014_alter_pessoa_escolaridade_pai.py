# Generated by Django 3.2.6 on 2021-09-02 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20210902_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='escolaridade_pai',
            field=models.IntegerField(blank=True, choices=[(1, 'Ensino Fundamental Incompleto'), (2, 'Ensino Fundamental Completo'), (3, 'Ensino Médio Incompleto'), (4, 'Ensino Médio Completo'), (5, 'Ensino Superior Incompleto'), (6, 'Ensino Superior Completo'), (7, 'Pós-Graduação'), (8, 'Mestrado'), (9, 'Doutorado')], null=True, verbose_name='Escolaridade do Pai'),
        ),
    ]