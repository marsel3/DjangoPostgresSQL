# Generated by Django 4.2 on 2023-04-29 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CreateDatabase', '0008_alter_sportsmen_sportsmen_vidporta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sportsmen',
            name='sportsmen_vidporta',
        ),
    ]