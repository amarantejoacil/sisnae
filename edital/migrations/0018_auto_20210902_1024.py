# Generated by Django 3.2.6 on 2021-09-02 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edital', '0017_alter_edital_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='edital',
            old_name='data_fim',
            new_name='data_hora_fim',
        ),
        migrations.RenameField(
            model_name='edital',
            old_name='data_inicio',
            new_name='data_hora_inicio',
        ),
    ]