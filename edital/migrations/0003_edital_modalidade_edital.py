# Generated by Django 3.2.6 on 2021-09-02 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edital', '0002_modalidadeedital'),
    ]

    operations = [
        migrations.AddField(
            model_name='edital',
            name='modalidade_edital',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='edital.modalidadeedital'),
            preserve_default=False,
        ),
    ]