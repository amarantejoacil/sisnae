# Generated by Django 3.2.6 on 2021-09-01 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edital', '0002_edital_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edital',
            name='numero',
            field=models.PositiveIntegerField(verbose_name='Nº do Edital'),
        ),
    ]
