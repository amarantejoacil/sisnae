# Generated by Django 3.2.6 on 2021-09-02 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscricao', '0013_auto_20210902_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscricao',
            name='situacao',
        ),
    ]
