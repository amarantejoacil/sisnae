# Generated by Django 3.2.6 on 2021-09-02 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edital', '0019_edital_edital_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='EtapaEdital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IncPor', models.IntegerField(blank=True, null=True, verbose_name='Incluido Por')),
                ('AltPor', models.IntegerField(blank=True, null=True, verbose_name='Alterado Por')),
                ('IncEm', models.DateTimeField(auto_now_add=True, verbose_name='Incluido Em')),
                ('AltEm', models.DateTimeField(auto_now=True, verbose_name='Alterado Em')),
                ('descricao', models.CharField(max_length=150, verbose_name='Descrição')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EditalAnexo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IncPor', models.IntegerField(blank=True, null=True, verbose_name='Incluido Por')),
                ('AltPor', models.IntegerField(blank=True, null=True, verbose_name='Alterado Por')),
                ('IncEm', models.DateTimeField(auto_now_add=True, verbose_name='Incluido Em')),
                ('AltEm', models.DateTimeField(auto_now=True, verbose_name='Alterado Em')),
                ('etapa_edital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edital.etapaedital')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
