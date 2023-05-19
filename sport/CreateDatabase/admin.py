from django.contrib import admin
from .models import *
# Register your models here.


class UsersAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_fullname', 'user_status')
    list_display_links = ('user_name', 'user_fullname', 'user_status')
    search_fields = ('user_name', 'user_fullname', 'user_status')


class SportsmenAdmin(admin.ModelAdmin):
    list_display = ('sportsmen_fio', 'sportsmen_age', 'sportsmen_team')
    list_display_links = ('sportsmen_fio', 'sportsmen_age', 'sportsmen_team')
    search_fields = ('sportsmen_fio', 'sportsmen_team')




class TrenerAdmin(admin.ModelAdmin):
    list_display = ('trener_tg', 'trener_fio', 'trener_passport', 'trener_kval')
    list_display_links = ('trener_tg', 'trener_fio', 'trener_passport', 'trener_kval')
    search_fields = ('trener_tg', 'trener_fio', 'trener_passport', 'trener_kval')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'team_vidsporta', 'team_trener')
    list_display_links = ('team_name', 'team_vidsporta', 'team_trener')
    search_fields = ('team_name', 'team_vidsporta', 'team_trener')



class VidSportaAdmin(admin.ModelAdmin):
    list_display = ('vidsporta_name', 'vidsporta_type')
    list_display_links = ('vidsporta_name', 'vidsporta_type')
    search_fields = ('vidsporta_name', 'vidsporta_type')


class StadionAdmin(admin.ModelAdmin):
    list_display = ('stadion_name', 'stadion_addres', 'stadion_capacity')
    list_display_links = ('stadion_name', 'stadion_addres', 'stadion_capacity')
    search_fields = ('stadion_name', 'stadion_addres')


class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('competition_vidsporta', 'competition_team', 'competition_mesto')
    list_display_links = ('competition_vidsporta', 'competition_team', 'competition_mesto')
    search_fields = ('competition_vidsporta', 'competition_team', 'competition_mesto')

class GamesAdmin(admin.ModelAdmin):
    list_display = ('games_vidsporta', 'games_date', 'games_place')
    list_display_links = ('games_vidsporta', 'games_date', 'games_place')
    search_fields = ('games_vidsporta', 'games_date', 'games_place')


class ResultsSoloAdmin(admin.ModelAdmin):
    list_display = ('resultsolo_id', 'resultsolo_solo', 'game_result')
    list_display_links = ('resultsolo_id', 'resultsolo_solo', 'game_result')
    search_fields = ('resultsolo_solo', 'game_result')


class ResultsTeamAdmin(admin.ModelAdmin):
    list_display = ('resultteam_team1', 'resultteam_team2', 'resultteam_result')
    list_display_links = ('resultteam_team1', 'resultteam_team2', 'resultteam_result')
    search_fields = ('resultteam_team1', 'resultteam_team2')


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_name',)
    list_display_links = ('subject_name',)
    search_fields = ('subject_name',)


admin.site.register(Users, UsersAdmin)
admin.site.register(Sportsmen, SportsmenAdmin)
admin.site.register(Trener, TrenerAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(VidSporta, VidSportaAdmin)
admin.site.register(Stadion, StadionAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Games, GamesAdmin)
admin.site.register(ResultsSolo, ResultsSoloAdmin)
admin.site.register(ResultsTeam, ResultsTeamAdmin)
admin.site.register(Subject, SubjectAdmin)