# Generated by Django 4.2 on 2023-05-13 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CreateDatabase', '0014_alter_sportsmen_sportsmen_vidsporta'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportsmen',
            name='sportsmen_trener',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='CreateDatabase.trener', verbose_name='Тренер'),
        ),
    ]
