# Generated by Django 3.2.6 on 2021-10-06 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_pessoa_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='cpf',
            field=models.CharField(max_length=15, verbose_name='CPF'),
        ),
    ]
