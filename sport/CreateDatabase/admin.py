from django.contrib import admin
from .models import *
# Register your models here.


class AdminAdmin(admin.ModelAdmin):
    list_display = ('admin_fio', 'admin_login')
    list_display_links = ('admin_fio', 'admin_login')
    search_fields = ('admin_fio', 'admin_login')


class SportsmenAdmin(admin.ModelAdmin):
    list_display = ('sportsmen_fio', 'sportsmen_age', 'sportsmen_team')
    list_display_links = ('sportsmen_fio', 'sportsmen_age', 'sportsmen_team')
    search_fields = ('sportsmen_fio', 'sportsmen_team')


class TrenerAdmin(admin.ModelAdmin):
    list_display = ('trener_fio', 'trener_passport', 'trener_kval', 'trener_team')
    list_display_links = ('trener_fio', 'trener_passport', 'trener_kval', 'trener_team')
    search_fields = ('trener_fio', 'trener_kval', 'trener_team')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'team_vidsporta', 'team_trener', 'team_type')
    list_display_links = ('team_name', 'team_vidsporta', 'team_trener', 'team_type')
    search_fields = ('team_name', 'team_vidsporta', 'team_trener', 'team_type')


class VidSportaAdmin(admin.ModelAdmin):
    list_display = ('vidsporta_name', )
    list_display_links = ('vidsporta_name', )
    search_fields = ('vidsporta_name', )


class StadionAdmin(admin.ModelAdmin):
    list_display = ('stadion_name', 'stadion_addres', 'stadion_capacity')
    list_display_links = ('stadion_name', 'stadion_addres', 'stadion_capacity')
    search_fields = ('stadion_name', 'stadion_addres')


class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('competition_vidsporta', 'competition_date', 'competition_team', 'competition_mesto', 'competition_place')
    list_display_links = ('competition_vidsporta', 'competition_date', 'competition_team', 'competition_mesto', 'competition_place')
    search_fields = ('competition_vidsporta', 'competition_date', 'competition_team', 'competition_place')


class GamesAdmin(admin.ModelAdmin):
    list_display = ('games_vidsporta', 'games_date', 'games_place')
    list_display_links = ('games_vidsporta', 'games_date', 'games_place')
    search_fields = ('games_vidsporta', 'games_date', 'games_place')


class ResultsSoloAdmin(admin.ModelAdmin):
    list_display = ('resultsolo_solo', 'game_result')
    list_display_links = ('resultsolo_solo', 'game_result')
    search_fields = ('resultsolo_solo', 'game_result')


class ResultsTeamAdmin(admin.ModelAdmin):
    list_display = ('resultteam_team1', 'resultteam_team2', 'resultteam_result')
    list_display_links = ('resultteam_team1', 'resultteam_team2', 'resultteam_result')
    search_fields = ('resultteam_team1', 'resultteam_team2')



admin.site.register(Admin, AdminAdmin)
admin.site.register(Sportsmen, SportsmenAdmin)
admin.site.register(Trener, TrenerAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(VidSporta, VidSportaAdmin)
admin.site.register(Stadion, StadionAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Games, GamesAdmin)
admin.site.register(ResultsSolo, ResultsSoloAdmin)
admin.site.register(ResultsTeam, ResultsTeamAdmin)
