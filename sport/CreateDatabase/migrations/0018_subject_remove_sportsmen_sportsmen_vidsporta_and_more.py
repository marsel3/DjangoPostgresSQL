# Generated by Django 4.2 on 2023-05-13 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CreateDatabase', '0017_alter_sportsmen_sportsmen_trener'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_name', models.TextField(primary_key=True, serialize=False, unique=True, verbose_name='Вид субъекта')),
            ],
            options={
                'verbose_name': 'Вид субъекта',
                'verbose_name_plural': 'Виды субъекта',
                'ordering': ['subject_name'],
            },
        ),
        migrations.RemoveField(
            model_name='sportsmen',
            name='sportsmen_vidsporta',
        ),
        migrations.AlterField(
            model_name='sportsmen',
            name='sportsmen_team',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='CreateDatabase.team', verbose_name='Команда'),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_name',
            field=models.TextField(unique=True, verbose_name='Название команды'),
        ),
        migrations.AddField(
            model_name='team',
            name='team_subject',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='CreateDatabase.subject', verbose_name='Вид субъекта'),
        ),
    ]
