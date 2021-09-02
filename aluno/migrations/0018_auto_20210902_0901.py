# Generated by Django 3.2.6 on 2021-09-02 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0017_auto_20210902_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='aluno_gestante',
            field=models.BooleanField(default=False, verbose_name='Medicamentos de Uso Regular?'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='aluno_transporte',
            field=models.IntegerField(choices=[(1, 'Transporte Coletivo'), (2, 'Van'), (3, 'Carro'), (4, 'Moto'), (5, 'A pé'), (6, 'Carona'), (7, 'Bicicleta')], default=1, verbose_name='Informe o meio de transporte utilizado para chegar ao Campus?'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aluno',
            name='aluno_dist_escola',
            field=models.IntegerField(choices=[(1, 'Aproximadamente 1km'), (2, 'Aproximadamente 2.5km'), (3, 'Aproximadamente 5km'), (4, 'Aproximadamente 7.5km'), (5, 'Aproximadamente 10km'), (6, 'Aproximadamente 12.5km'), (7, 'Aproximadamente 15km'), (8, 'Aproximadamente 17.5km'), (9, 'Aproximadamente 20km'), (10, 'Aproximadamente 30km'), (11, 'Acima de 30km')], verbose_name='Distância aproximada da residência ao Campus em KM?'),
        ),
    ]
