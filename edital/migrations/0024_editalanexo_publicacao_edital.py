# Generated by Django 3.2.6 on 2021-09-02 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edital', '0023_auto_20210902_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='editalanexo',
            name='publicacao_edital',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='edital.publicacaoedital'),
            preserve_default=False,
        ),
    ]
