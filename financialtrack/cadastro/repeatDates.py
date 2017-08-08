from calendar import monthrange
import datetime
from .models import Transacoes

class RepeatTransaction(object):
    """This class controls all the data to be inserted, delete or updated 
    in Transacoes's model that has future dates.
    """
 
    def createRepeatedTransactions(self, months, original_date, post_content, user):
        """Method called upon the creation of Transacoes objects which
        has future dates.
        """
        for i in range(months-1):
            original_date = self.__monthIncrement(original_date, i+1)
            Transacoes(estabelecimento = post_content['estabelecimento'],
                    despesa = post_content['despesa'],
                    tipo_trans = post_content['tipo_trans'],
                    data = original_date,
                    valor = post_content['valor'],
                    informacoes = post_content['informacoes'],
                    incluido_por = user,
                    repeat = True,
                    total_repeats = months).save()

    def manageRepeated(self, pk, update=None):
        """Updates values or delete transactions related to the Transaction
        been updated.
        """
        transacao = Transacoes.objects.get(pk=pk)
        if transacao.repeat:
            months = transacao.total_repeats
            repeated = Transacoes.objects.filter(estabelecimento = transacao.estabelecimento,
                                                 despesa = transacao.despesa,
                                                 tipo_trans = transacao.tipo_trans,
                                                 valor = transacao.valor,
                                                 incluido_por = transacao.incluido_por,
                                                 repeat = True,
                                                 total_repeats = months
                                                ).exclude(pk=pk)

            future = repeated.exclude(data__lte=transacao.data)
            old = repeated.exclude(data__gte=transacao.data)

            if update:
                future.update(**update)
                future.update(total_repeats=len(repeated)-len(old))
                old.update(total_repeats=len(old))


            else:
                future.delete()
                old.update(total_repeats=len(old))

    def __monthIncrement(self, old_date, month):
        """Increments a date or datetime by one month
        """
        total_days = monthrange(old_date.year,old_date.month)[-1]
        new_date = old_date+datetime.timedelta(total_days)

        if total_days == old_date.day:
            """Incmrements a date or datetime based on the 
            the last day for each month"""
            new_date = old_date + datetime.timedelta(1)
            new_date = new_date.replace(
                day=monthrange(new_date.year, new_date.month)[-1])

        return new_date
