#*-*coding:utf-8 *-*
from django.contrib import admin
from .models import NavMenu, MainMenu

class NavMenuAdmin(admin.ModelAdmin):
    list_display = ['nome']

class MainMenuAdmin(admin.ModelAdmin):
    list_display = ['nome']


admin.site.register(NavMenu, NavMenuAdmin)
admin.site.register(MainMenu, MainMenuAdmin)




