# Generated by Django 3.2.6 on 2021-10-01 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0006_remove_questionario_edital'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionario',
            name='aluno',
        ),
    ]
