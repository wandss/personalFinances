#*-*coding:utf-8 *-*
from .models import NavMenu

def menu(request):
    nav_menu = NavMenu.objects.all()
    return {'nav_menu':nav_menu}
