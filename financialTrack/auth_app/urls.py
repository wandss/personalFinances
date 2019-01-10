from django.urls import path
from .views import LoginAPIView

app_name = 'auth_app'

urlpatterns = [
    path('', LoginAPIView.as_view(), name='login'),
]
