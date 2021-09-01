# Generated by Django 3.2.6 on 2021-09-01 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edital', '0010_remove_edital_ano'),
    ]

    operations = [
        migrations.AddField(
            model_name='edital',
            name='ano',
            field=models.PositiveIntegerField(default=1, verbose_name='Informe o ano do Edital'),
            preserve_default=False,
        ),
    ]
