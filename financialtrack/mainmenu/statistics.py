from collections import OrderedDict
from decimal import Decimal, ROUND_DOWN
from datetime import datetime
from django.db.models import Sum
from cadastro.models import Transacoes

class Statistics(object):
    """Makes some caulculations to generates statistical data 
    based on data base's information.
    """

    def __init__(self, user, current_date):
        self.current_date = current_date 
        self.user = user

    def summarizedData(self, month=False):
        """Shows the totals for money expent, received and 
        calculates the balance for the current month and also
        for all transacations for the given user.
        """
        current = OrderedDict()

        if month:
            query_set = Transacoes.objects.filter(
                incluido_por=self.user,
                data__lte=self.current_date,
                data__year=self.current_date.year,
                data__month=self.current_date.month
            )

        else:
            query_set = Transacoes.objects.filter(
                    data__lte=self.current_date,
                    incluido_por=self.user)

        credit = query_set.filter(tipo_trans=2).aggregate(
                Sum('valor'))['valor__sum']
        debit = query_set.filter(tipo_trans=1).aggregate(
                Sum('valor'))['valor__sum']

        if credit is None:
            credit = 0
        if debit is None:
            debit = 0

        saldo = credit - debit
        current['Crédito'] = credit
        current['Débito'] = debit
        current['Saldo'] = saldo

        return current

    def summarizedFutureExpenses(self):
        """Group, calculates and return a dictionary with
        transactions that has 'data' attribute bigger than 
        the current date, for the given user.
        """
        future_expenses = OrderedDict()
        label = OrderedDict()


        all_future_payments = Transacoes.objects.filter(
            incluido_por=self.user,
            data__gte=self.current_date).values(
                'estabelecimento','valor','total_repeats','data')

        for est in set([result['estabelecimento'] for result in 
                        all_future_payments]):

            results = all_future_payments.filter(estabelecimento=est)
            total = results.aggregate(Sum('valor'))['valor__sum']
            parcelas = results.count()
            pago = results.filter(data__year__lte=self.current_date.year,
                data__month__lte=self.current_date.month).count()
            due_payments = (total - (pago * (total/parcelas))).quantize(
                    Decimal('1.00'), rounding=ROUND_DOWN)

            future_expenses[est] = {
                'Total': total, 
                'Parcelas': parcelas,
                'Pagas': pago,
                'Restante': due_payments
            }
            
        return future_expenses                                    

    def getYearMonths(self):
        """Query the database for all Transactions and makes 
        a dictionary, grouping than by year and month.
        """
        year_months = OrderedDict()
        transacoes = Transacoes.objects.filter(
            incluido_por=self.user).order_by('data')

        years = [year for year in set([trans.data.year for trans in
                                       transacoes])]
        for year in years:
            if year not in year_months:
                year_months[year] = [res for res in set([
                    trs.data.month for trs in transacoes.filter(
                        data__year=year)])]

        [values.sort() for values in year_months.values()]

        for key, value in year_months.items():
            for i, v in enumerate(value):
                value[i] = datetime.strptime('01/{}/{}'.format(v,key),
                                            '%d/%m/%Y')
        return year_months                
