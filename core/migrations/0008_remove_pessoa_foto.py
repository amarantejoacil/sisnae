# Generated by Django 3.2.6 on 2021-09-02 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_pessoa_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='foto',
        ),
    ]
