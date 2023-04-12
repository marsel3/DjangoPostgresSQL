from django.db import models

# Create your models here.
class Sportsmen(models.Model):
    sportsmen_id = models.AutoField(primary_key=True)
    sportsmen_fio = models.CharField(max_length=255, verbose_name='ФИО')
    sportsmen_age = models.IntegerField(verbose_name='Возраст')
    sportsmen_team = models.ForeignKey('Team', on_delete=models.PROTECT, verbose_name="Команда")

    def __str__(self):
        return self.sportsmen_fio
    
    class Meta:
        verbose_name = 'Спортсмен'
        verbose_name_plural = 'Спортсмены'
        ordering = ['sportsmen_fio', 'sportsmen_age']


class Trener(models.Model):
    trener_id = models.AutoField(primary_key=True)
    trener_fio = models.CharField(max_length=255, verbose_name='ФИО')
    trener_passport = models.TextField(verbose_name='Паспорт')
    trener_kval = models.TextField(verbose_name='Квалификация')
    trener_team = models.TextField(verbose_name='Команда')

    def __str__(self):
        return self.trener_fio

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренеры'
        ordering = ['trener_fio']


class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    team_name = models.TextField(verbose_name='Название команды')
    team_vidsporta = models.ForeignKey('VidSporta', on_delete=models.PROTECT, verbose_name='Вид спорта')
    team_trener = models.ForeignKey('Trener', on_delete=models.PROTECT, verbose_name='Тренер')
    team_type = models.BooleanField(default=False, verbose_name='Командный или НЕТ')

    def __str__(self):
        return self.team_name
    
    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'
        ordering = ['team_vidsporta', 'team_name']

class VidSporta(models.Model):
    vidsporta_name = models.TextField(primary_key=True,  verbose_name='Вид спорта')

    def __str__(self):
        return self.vidsporta_name

    class Meta:
        verbose_name = 'Вид спорта'
        verbose_name_plural = 'Виды спорта'
        ordering = ['vidsporta_name']


class Stadion(models.Model):
    stadion_name = models.TextField(primary_key=True)
    stadion_addres = models.TextField(verbose_name='Адрес')
    stadion_capacity = models.IntegerField(verbose_name='Вместимость')

    def __str__(self):
        return self.stadion_name
    
    class Meta:
        verbose_name = 'Стадион'
        verbose_name_plural = 'Стадионы'
        ordering = ['stadion_name']


class Competition(models.Model):
    competition_vidsporta = models.ForeignKey('VidSporta', on_delete=models.PROTECT, verbose_name='Вид спорта')
    competition_date = models.DateField(verbose_name='Дата')
    competition_team = models.ForeignKey('Team', on_delete=models.PROTECT, verbose_name='Команда')
    competition_mesto = models.IntegerField(verbose_name="Место победителя")
    competition_place = models.ForeignKey('Stadion', on_delete=models.PROTECT, verbose_name='Место проведения')

    class Meta:
        verbose_name = 'Финальный результат'
        verbose_name_plural = 'Финальные результаты'
        ordering = ['competition_vidsporta', 'competition_date']


class Games(models.Model):
    games_id = models.AutoField(primary_key=True)
    games_vidsporta = models.ForeignKey('VidSporta', on_delete=models.PROTECT, verbose_name='Вид спорта')
    games_date = models.DateField(verbose_name='Дата')
    games_place = models.ForeignKey('Stadion', on_delete=models.PROTECT, verbose_name='Место проведения')

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
        ordering = ['games_vidsporta', 'games_date']


class ResultsTeam(models.Model):
    resultteam_id = models.ForeignKey('Games', on_delete=models.PROTECT)
    resultteam_team1 = models.ForeignKey('Team', on_delete=models.PROTECT, verbose_name='Команда 1', related_name='+')
    resultteam_team2 = models.ForeignKey('Team', on_delete=models.PROTECT, verbose_name='Команда 2', related_name='+')
    resultteam_result = models.ForeignKey('Team', on_delete=models.PROTECT, verbose_name='Победитель', related_name='+')

    class Meta:
        verbose_name = 'Промежуточный результат команд'
        verbose_name_plural = 'Промежуточные результаты команд'
        ordering = ['resultteam_id']


class ResultsSolo(models.Model):
    resultsolo_id = models.ForeignKey('Games', on_delete=models.PROTECT)
    resultsolo_solo = models.ForeignKey('Team', on_delete=models.PROTECT, verbose_name='ФИО игрока')
    game_result = models.IntegerField(verbose_name='Результаты')

    class Meta:
        verbose_name = 'Промежуточный результат соло'
        verbose_name_plural = 'Промежуточные результаты соло'
        ordering = ['resultsolo_id']


class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_fio = models.TextField(verbose_name='ФИО')
    admin_login = models.CharField(max_length=255, verbose_name='Логин')
    admin_password = models.CharField(max_length=255, verbose_name='Пароль')

    def __str__(self):
        return self.admin_login

    class Meta:
        verbose_name = 'Админ'
        verbose_name_plural = 'Админы'
        ordering = ['admin_login', 'admin_fio']
