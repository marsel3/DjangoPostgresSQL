# Generated by Django 4.2 on 2023-04-29 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CreateDatabase', '0012_alter_sportsmen_sportsmen_vidporta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sportsmen',
            old_name='sportsmen_vidporta',
            new_name='sportsmen_vidsporta',
        ),
    ]