# Generated by Django 4.2 on 2023-04-29 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CreateDatabase', '0004_alter_trener_trener_passport'),
    ]

    operations = [
        migrations.AddField(
            model_name='vidsporta',
            name='vidsporta_type',
            field=models.BooleanField(default=False, verbose_name='Командный или НЕТ'),
        ),
    ]
