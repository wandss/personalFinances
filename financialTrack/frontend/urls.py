from django.urls import re_path
from .views import (NavMenuView, MainMenuAPIView, AppDataListAPIView)

app_name = 'frontend'

urlpatterns = [
    re_path(r'^navmenu/', NavMenuView.as_view(), name='navmenu'),
    re_path(r'^mainmenu/', MainMenuAPIView.as_view(), name='mainmenu'),
    re_path(r'^appdata/', AppDataListAPIView.as_view(), name="appdata"),
]
