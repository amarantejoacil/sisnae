# Generated by Django 3.2.6 on 2021-09-02 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscricao', '0007_inscricao_edital'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscricao',
            name='edital',
        ),
    ]
