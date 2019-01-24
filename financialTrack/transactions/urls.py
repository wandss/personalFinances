from django.urls import path
from .views import (ExpenseTypeView, ExpenseTypeUpdateDeleteView,
                    TransactionsListCreateView,
                    TransactionsListUpdateDeleteView,
                    OperationTypeListView, NavByDateListView,
                    TransactionsYearListAPIView,
                    TransactionsYearMonthListAPIView,
                   )

app_name = 'transactions'
urlpatterns = [
    path('', TransactionsListCreateView.as_view(), name='transactions'),
    path('<int:pk>',TransactionsListUpdateDeleteView.as_view(),
         name='transaction'),
    path('year/<int:year>', TransactionsYearListAPIView.as_view(),
        name='transactions_year'),
    path('year/<int:year>/month/<int:month>',
        TransactionsYearMonthListAPIView.as_view()),
    path('expensetypes/', ExpenseTypeView.as_view(), name='expensetypes'),
    path('expensetypes/<int:pk>', ExpenseTypeUpdateDeleteView.as_view(),
         name='expensetype'),
    path('operationtypes/', OperationTypeListView.as_view(),
         name='operationtype'),
    path('navbydate/', NavByDateListView.as_view(), name='navbydate'),
]
