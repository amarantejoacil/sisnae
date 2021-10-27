# Generated by Django 3.2.6 on 2021-10-27 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscricao', '0008_inscricao_semestre'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscricao',
            name='inscri_quest_alu_dist_escola',
            field=models.IntegerField(choices=[(1, 'Aproximadamente 1km'), (2, 'Aproximadamente 2.5km'), (3, 'Aproximadamente 5km'), (4, 'Aproximadamente 7.5km'), (5, 'Aproximadamente 10km'), (6, 'Aproximadamente 12.5km'), (7, 'Aproximadamente 15km'), (8, 'Aproximadamente 17.5km'), (9, 'Aproximadamente 20km'), (10, 'Aproximadamente 30km'), (11, 'Acima de 30km')], default=1, verbose_name='Distância aproximada da residência ao Campus em KM?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inscricao',
            name='inscri_quest_alu_form_ingre',
            field=models.CharField(choices=[('A', 'Por Ampla Concorrência'), ('C', 'Por Meio de Cota')], default='A', max_length=1, verbose_name='Forma de Ingresso'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inscricao',
            name='inscri_quest_alu_gestante',
            field=models.BooleanField(default=False, verbose_name='Aluna está Gestante? '),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='inscri_quest_alu_lactante',
            field=models.BooleanField(default=False, verbose_name='Você é Lactante? '),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='inscri_quest_alu_medicacao',
            field=models.BooleanField(default=False, verbose_name='Medicamentos de Uso Regular?'),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='inscri_quest_alu_medicacao_cid',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Informe o CID (Classificação Internacional de Doenças)'),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='inscri_quest_alu_medicacao_desc',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Informe a medicação'),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='inscri_quest_alu_tempo_escola',
            field=models.IntegerField(choices=[(1, 'Aproximadamente 5 minutos'), (2, 'Aproximadamente 10 minutos'), (3, 'Aproximadamente 15 minutos'), (4, 'Aproximadamente 20 minutos'), (5, 'Aproximadamente 25 minutos'), (6, 'Aproximadamente 30 minutos'), (7, 'Aproximadamente 45 minutos'), (8, 'Aproximadamente 1 hora'), (9, 'Aproximadamente 1 hora e 30 minutos'), (10, 'Aproximadamente 2 horas'), (11, 'Acima de 2 horas')], default=1, verbose_name='Tempo que o (a) estudante gasta da sua residência ao Campus'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inscricao',
            name='inscri_quest_alu_transporte',
            field=models.IntegerField(choices=[(1, 'Transporte Coletivo'), (2, 'Van'), (3, 'Carro'), (4, 'Moto'), (5, 'A pé'), (6, 'Carona'), (7, 'Bicicleta')], default=1, verbose_name='Informe o meio de transporte utilizado para chegar ao Campus?'),
            preserve_default=False,
        ),
    ]