from django.shortcuts import render
from django.utils import timezone
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from transactions.models import Transactions
from chartData.serializers import ExpenseTypeTransactionsSerializer


class ExpenseTypeChartDataViewSet(ViewSet):
    def list(self, request):
        new_queryset = []
        months = []
        expense = request.GET.get('expense')
        queryset = Transactions.objects.filter(expense=expense,
                dt_creation__lte=timezone.now())
        years = list(set([query.dt_transaction.year for query in queryset]))
        years.sort()
        for year in years:
            months.append(list(set([q.dt_transaction.month
                for q in queryset.filter(dt_transaction__year=year)])))
            months[-1].sort()
            for m in months[-1]:
                new_queryset.append({
                    'id':'{}{}'.format(m, year),
                    'dt_transaction':'{}/{}'.format(m, year),
                    'amount':sum([amount.amount
                        for amount in queryset.filter(dt_transaction__year=year,
                        dt_transaction__month=m)])
                    })


        serializer = ExpenseTypeTransactionsSerializer(new_queryset,
                many=True)
        return Response(serializer.data)

"""
TODO
  If not queryset return Response 404
  Retrieve only data from specific user
  request.user
  Add authentication classes and isauthenticated

"""


