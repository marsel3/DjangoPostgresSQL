from django.contrib import admin
from .models import *
# Register your models here.


class AdminAdmin(admin.ModelAdmin):
    list_display = ('admin_fio', 'admin_login')
    list_display_links = ('admin_fio', 'admin_login')
    search_fields = ('admin_fio', 'admin_login')




admin.site.register(Admin, AdminAdmin)