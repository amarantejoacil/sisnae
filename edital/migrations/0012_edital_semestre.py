# Generated by Django 3.2.6 on 2021-09-07 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edital', '0011_remove_edital_edital_icone'),
    ]

    operations = [
        migrations.AddField(
            model_name='edital',
            name='semestre',
            field=models.IntegerField(choices=[(1, '1° Semestre'), (2, '2° Semestre')], default=1, verbose_name='Relacionado a qual semestre?'),
            preserve_default=False,
        ),
    ]
