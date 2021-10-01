# Generated by Django 3.2.6 on 2021-10-01 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edital', '0015_auto_20210928_1833'),
        ('aluno', '0012_auto_20210910_1740'),
        ('questionario', '0004_questionarioanexo_questionario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionario',
            name='aluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aluno.aluno'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='edital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='edital.edital'),
        ),
        migrations.AlterField(
            model_name='questionarioanexo',
            name='questionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='questionario.questionario'),
        ),
    ]