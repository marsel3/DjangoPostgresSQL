# Generated by Django 4.2 on 2023-04-29 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CreateDatabase', '0006_remove_team_team_type_alter_vidsporta_vidsporta_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportsmen',
            name='sportsmen_vidporta',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='CreateDatabase.vidsporta', verbose_name='Вид спорта'),
        ),
    ]