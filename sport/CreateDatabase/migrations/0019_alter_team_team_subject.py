# Generated by Django 4.2 on 2023-05-13 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CreateDatabase', '0018_subject_remove_sportsmen_sportsmen_vidsporta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='team_subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CreateDatabase.subject', verbose_name='Вид субъекта'),
        ),
    ]