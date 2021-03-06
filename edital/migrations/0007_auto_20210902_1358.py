# Generated by Django 3.2.6 on 2021-09-02 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edital', '0006_edital_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edital',
            name='modalidade_edital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='edital.modalidadeedital'),
        ),
        migrations.AlterField(
            model_name='edital',
            name='setor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='edital.setoredital'),
        ),
    ]
