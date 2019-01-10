from django.urls import path, re_path
from frontend.views import NavMenuView, MainMenuAPIView, AppView

app_name = 'frontend'

urlpatterns = [
    re_path(r'^navmenu/', NavMenuView.as_view(), name='navmenu'),
    re_path(r'^mainmenu/', MainMenuAPIView.as_view(), name='mainmenu'),
    re_path(r'[\s\S]*', AppView.as_view(), name='home'),
]
