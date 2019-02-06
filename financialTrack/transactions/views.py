import calendar
from datetime import datetime
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (ListAPIView,
                                     ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from transactions.models import ExpenseType, Transactions, OperationType
from transactions.serializers import (ExpenseTypeSerializer,
                                      TransactionsSerializer,
                                      OperationTypeSerializer)


class ExpenseTypeView(ListCreateAPIView):
    serializer_class = ExpenseTypeSerializer

    def get_queryset(self):
        return ExpenseType.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)


class ExpenseTypeUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseTypeSerializer

    def get_queryset(self):
        return ExpenseType.objects.filter(created_by=self.request.user)


class TransactionsListCreateView(ListCreateAPIView):
    serializer_class = TransactionsSerializer
    today = datetime.now()
    today = timezone.make_aware(today)

    def get_queryset(self):

        return Transactions.objects.filter(created_by=self.request.user)

#        if 'today' in self.request.query_params:
#
#            if 'old' in self.request.query_params:
#                date = self.request.query_params.get('old')
#                return queryset.filter(dt_transaction__lte=self.today)
#
#            if 'future' in self.request.query_params:
#                return queryset.filter(dt_transaction__gt=self.today)
#
#            return queryset.filter(dt_transaction__month=self.today.month,
#                    dt_transaction__year=self.today.year,
#                    dt_transaction__day__lte=self.today.day)
#
#        if 'year' in self.request.query_params:
#            year = int(self.request.query_params.get('year'))
#            month = int(self.request.query_params.get('month'))
#            day = calendar.monthrange(year, month)[-1]
#
#            if 'old' or 'future' in self.request.query_params:
#                reference_date = timezone.make_aware(
#                        datetime.strptime('{}{}{}'.format(day,month,year),
#                        "%d%m%Y"))
#                if 'old' in self.request.query_params:
#                    return queryset.filter(dt_transaction__lte=reference_date)
#
#                elif 'future' in self.request.query_params:
#                    return queryset.filter(dt_transaction__gte=reference_date)
#
#            return queryset.filter(dt_transaction__month=month,
#                    dt_transaction__year=year,
#                    dt_transaction__day__lte=day,
#                    created_by=self.request.user)
#
#        else:
#            return Transactions.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):

        return serializer.save(created_by=self.request.user)


class TransactionsYearListAPIView(ListAPIView):
    serializer_class = TransactionsSerializer

    def get_queryset(self):

        return Transactions.objects.filter(
            created_by=self.request.user,
            dt_transaction__year=self.kwargs.get('year'))


class TransactionsYearMonthListAPIView(ListAPIView):
    serializer_class = TransactionsSerializer

    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')

        return Transactions.objects.filter(
            created_by=self.request.user, dt_transaction__year=year,
            dt_transaction__month=month)


class TransactionsListUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer


class OperationTypeListView(ListAPIView):
    serializer_class = OperationTypeSerializer
    queryset = OperationType.objects.all()


class NavByDateListView(APIView):
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


"""
TODO:
    Close API to IsAdminUser only?

    Start paginating
    Improve NavByDateListView.
        use something like Transactions.objects.all().date('dt_transaction',
        'year')
        to return a list with dates?
        Then another to show available months for a giving year?

    Remove all those "ifs from TransactionsListCreateView" since now
        theres two specilized views that achieve the same that overthere
        has been done with query string


    Improve get_queryset method to filter transactions by date
    Set a way to keep refreshing JWT token while user is using the app
      the ideia is: Check if the experiation time is close, then, refresh
      the token

    Add creator property to models for transactions and Expensetype.
    Save user when creating property
    List only objects related to the user
    Check Django i18n for month names
"""
