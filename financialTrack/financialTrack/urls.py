from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_swagger.views import get_swagger_view
from chartData.urls import charts
from frontend.views import AppView

schema_view = get_swagger_view(title='Personal Finances API')

urlpatterns = [
    re_path('^api/v1/frontend/', include(
        'frontend.urls', namespace='frontend')),
    re_path('^api/v1/transactions/', include('transactions.urls',
                                             namespace='transactions')),
    re_path('^api/v1/charts/', include(charts)),
    path('api/v1/auth/', obtain_jwt_token),
    # path('api/v1/token/', include('auth_app.urls')),
    re_path('^admin', admin.site.urls),
    re_path(r'api/v1/docs/', schema_view),
    re_path(r'[\s\S]*', AppView.as_view()),
]
