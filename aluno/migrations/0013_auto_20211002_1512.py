# Generated by Django 3.2.6 on 2021-10-02 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0002_curso_curso_tipo'),
        ('core', '0001_initial'),
        ('aluno', '0012_auto_20210910_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='curso.curso'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='pessoa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.pessoa'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='semestre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='curso.semestre'),
        ),
    ]
