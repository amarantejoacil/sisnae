# Generated by Django 3.2.6 on 2021-09-02 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0023_alunoanexo_aluno_anexo_valor'),
    ]

    operations = [
        migrations.AddField(
            model_name='alunoanexo',
            name='aluno',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='aluno.aluno'),
            preserve_default=False,
        ),
    ]