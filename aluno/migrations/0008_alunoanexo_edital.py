# Generated by Django 3.2.6 on 2021-09-08 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edital', '0014_auto_20210907_2050'),
        ('aluno', '0007_alter_aluno_aluno_form_ingre'),
    ]

    operations = [
        migrations.AddField(
            model_name='alunoanexo',
            name='edital',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='edital.edital'),
            preserve_default=False,
        ),
    ]