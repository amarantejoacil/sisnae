# Generated by Django 3.2.6 on 2021-09-02 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edital', '0024_editalanexo_publicacao_edital'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacaoedital',
            name='anexo_arq',
            field=models.CharField(default='1', max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='EditalAnexo',
        ),
    ]