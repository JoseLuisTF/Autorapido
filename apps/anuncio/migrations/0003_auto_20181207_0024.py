# Generated by Django 2.1.3 on 2018-12-07 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anuncio', '0002_auto_20181207_0013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anuncio',
            old_name='user',
            new_name='vendedor',
        ),
    ]