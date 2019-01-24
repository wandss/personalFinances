from rest_framework.routers import DefaultRouter
from .views import ExpenseTypeChartDataViewSet

app_name = 'chartData'
router = DefaultRouter()
router.register(r'expensetype', ExpenseTypeChartDataViewSet,
        base_name="expesetypechart")

charts = router.urls
