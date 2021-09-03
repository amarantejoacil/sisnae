# Generated by Django 3.2.6 on 2021-09-03 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0003_alter_aluno_aluno_form_ingre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='aluno_dist_escola',
            field=models.BigIntegerField(choices=[(1, 'Aproximadamente 1km'), (2, 'Aproximadamente 2.5km'), (3, 'Aproximadamente 5km'), (4, 'Aproximadamente 7.5km'), (5, 'Aproximadamente 10km'), (6, 'Aproximadamente 12.5km'), (7, 'Aproximadamente 15km'), (8, 'Aproximadamente 17.5km'), (9, 'Aproximadamente 20km'), (10, 'Aproximadamente 30km'), (11, 'Acima de 30km')], verbose_name='Distância aproximada da residência ao Campus em KM?'),
        ),
    ]