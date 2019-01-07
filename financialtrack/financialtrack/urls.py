"""financialTrack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_jwt.views import obtain_jwt_token
from chartData.urls import charts

urlpatterns = [
    re_path('^api/v1/frontend/', include('frontend.urls',namespace='frontend')),
    re_path('^api/v1/transactions/', include('transactions.urls',
                                        namespace='transactions')),
    re_path('^api/v1/charts/', include(charts)),
    path('api/v1/auth/', obtain_jwt_token),
    path('api/v1/token/', include('auth_app.urls')),
    #re_path('^api/v1/auth/',include('auth_app.urls', namespace="authentication")),
    re_path('^admin', admin.site.urls),
    re_path(r'[\s\S]*', include('frontend.urls', namespace="app")),
]
