# Generated by Django 3.2.6 on 2021-09-08 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0003_questionarioanexo'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionarioanexo',
            name='questionario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='questionario.questionario'),
            preserve_default=False,
        ),
    ]