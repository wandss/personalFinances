import calendar
from datetime import datetime
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (ListAPIView,
                                     ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework import status
from transactions.models import ExpenseType, Transactions, OperationType
from transactions.serializers import (ExpenseTypeSerializer,
                                      TransactionsSerializer,
                                      OperationTypeSerializer)


class ExpenseTypeView(ListCreateAPIView):
    """List all expense types."""
    serializer_class = ExpenseTypeSerializer

    def get_queryset(self):
        return ExpenseType.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)


class ExpenseTypeUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """Retrieve and destroy expense type."""
    serializer_class = ExpenseTypeSerializer

    def get_queryset(self):
        return ExpenseType.objects.filter(created_by=self.request.user)


class TransactionsListCreateView(ListCreateAPIView):
    """List and create transactions"""
    serializer_class = TransactionsSerializer
    today = datetime.now()
    today = timezone.make_aware(today)

    def get_queryset(self):

        return Transactions.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):

        return serializer.save(created_by=self.request.user)


class TransactionsYearListAPIView(ListAPIView):
    """List transactions for a given year."""
    serializer_class = TransactionsSerializer

    def get_queryset(self):

        return Transactions.objects.filter(
            created_by=self.request.user,
            dt_transaction__year=self.kwargs.get('year'))


class TransactionsYearMonthListAPIView(ListAPIView):
    """List transactions for specific month and year"""
    serializer_class = TransactionsSerializer

    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')

        return Transactions.objects.filter(
            created_by=self.request.user, dt_transaction__year=year,
            dt_transaction__month=month)


class TransactionsListUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """Get, update and delete transactions"""
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer


class OperationTypeListView(ListAPIView):
    """List operaion types."""
    serializer_class = OperationTypeSerializer
    queryset = OperationType.objects.all()


class NavByDateListView(APIView):
    """List all years and months from transactions in order to create
    a navigation menu"""
    def get(self, request):
        nav_by_date = []
        years = list(set([transaction.dt_transaction.year
                         for transaction in Transactions.objects.filter(
                            created_by=request.user)]))
        years.sort()

        for year in years:
            months = list((set(
                [transaction.dt_transaction.month for transaction in
                 Transactions.objects.filter(dt_transaction__year=year,
                                             created_by=request.user)])))
            months.sort()
            months = [{'id': month, 'name': calendar.month_name[month]}
                      for month in months]

            nav_by_date.append({'id': year,
                                'label': str(year),
                                'submenu': months})

        return Response(nav_by_date)


class TransactionsTotals(APIView):
    """Calculate values from transations based on given year and month"""

    def get(self, *args, **kwargs):
        year = kwargs.get('year')
        month = kwargs.get('month')

        transactions = Transactions.objects.filter(
            created_by=self.request.user,
            dt_transaction__year__lte=year,
            dt_transaction__month__lte=month,
        )

        expenses = sum([expenses.amount
                        for expenses in transactions.filter(operation_type=1)])

        income = sum([expenses.amount
                      for expenses in transactions.filter(operation_type=2)])

        data = {'income': income, 'expenses': expenses,
                'balance': income - expenses}

        return Response(data=data, status=status.HTTP_200_OK)


"""
TODO:
    Start paginating
    Improve NavByDateListView.
        use something like Transactions.objects.all().date('dt_transaction',
        'year')
        to return a list with dates?
        Then another to show available months for a giving year?

    Improve get_queryset method to filter transactions by date
    Set a way to keep refreshing JWT token while user is using the app
      the ideia is: Check if the experiation time is close, then, refresh
      the token

    Add creator property to models for transactions and Expensetype.
    Save user when creating property
    List only objects related to the user
    Check Django i18n for month names
"""
