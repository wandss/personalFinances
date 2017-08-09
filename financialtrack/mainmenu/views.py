#*-* coding:utf-8 *-*
from calendar import monthrange
from django.shortcuts import render, redirect
from django.db.models.deletion import ProtectedError
from django.views import generic
from django.utils import timezone
from django.contrib.auth import logout
from mainmenu.models import MainMenu
from cadastro.models import TipoDespesa, Transacoes
from cadastro.choices import tipo_choices
from cadastro.repeatDates import RepeatTransaction
from mainmenu.statistics import Statistics


class MenuView(generic.View):
    def get(self, request):
        context = {'page_title':'Opções Disponíveis:'}
        options = MainMenu.objects.all()
        context['options'] = options
        return render(request, 'main.html',context)


class DespesasView(generic.View):
    def get(self, request):
        context = {'page_title':'Despesas'}
        current_date = timezone.localtime(timezone.now())
        despesas = TipoDespesa.objects.filter(
            incluido_por=request.user)
        context['result_set'] = despesas
        stats = Statistics(request.user, current_date)

        context['years_list'] = stats.getYearMonths()
        return render(request, 'models_list.html', context)

class TransacoesView(generic.View):
    def get(self, request, **kwargs):
        year = kwargs.get('year')
        month = kwargs.get('month')
        current_date = timezone.localtime(timezone.now())
        context = {'page_title':'Transacoes'}

        if year:
            current_date = current_date.replace(year = int(year))
            current_date = current_date.replace(month = int(month))
            current_date = current_date.replace(
                    day=monthrange(int(year), int(month))[-1])


        transacoes = Transacoes.objects.filter(data__year=current_date.year,
                data__month=current_date.month,incluido_por=request.user,
                data__day__lte=current_date.day)
        
        stats = Statistics(request.user, current_date)
        
        context['history'] = stats.summarizedData()
        context['future_expenses'] = stats.summarizedFutureExpenses()
        context['current_month'] = stats.summarizedData(month=True)
        context['years_list'] = stats.getYearMonths()
        context['result_set'] = transacoes
        context['current_date'] = current_date

        return render(request, 'models_list.html', context)

class DespesaUpdate(generic.edit.UpdateView):
    model = TipoDespesa
    fields = ['nome']
    success_url = '/menu/Despesas'

    def get_context_data(self, **kwargs):
        context = super(DespesaUpdate, self).get_context_data(**kwargs)
        context['page_title'] = 'Alterar:'
        return context

class DespesaDelete(generic.edit.DeleteView):
    model = TipoDespesa
    template_name = 'cadastro/confirm_delete.html'
    success_url = '/menu/Despesas'

    def post(self, request, **kwargs):
        if 'cancel' in request.POST:
            return redirect('/menu/Despesas')
        else:
            try:
                return super(DespesaDelete, self).post(request, **kwargs)
            except ProtectedError:
                print('Adicionar Messagem informativa.')
                print(ProtectedError)
                #Adicionar template para mostrar erros
                return redirect('/menu/Despesas')

class TransacaoUpdate(generic.edit.UpdateView):
    model = Transacoes
    fields = ['estabelecimento','despesa','tipo_trans',
              'valor','informacoes','total_repeats','data']
    success_url = '/menu/Transacoes'

    def get_context_data(self, **kwargs):
        context = super(TransacaoUpdate, self).get_context_data(**kwargs)
        context['page_title'] = 'Alterar:'
        despesas = list(TipoDespesa.objects.all())
        despesas.insert(0, despesas.pop(despesas.index(self.object.despesa)))
        context['despesas'] = despesas

        if self.object.tipo_trans not in tipo_choices[0]:
            tipo_choices.insert(0, tipo_choices.pop(1))
        context['tipo_trans'] = tipo_choices 

        return context
    
    def form_valid(self, form):
        transacao = form.save(commit=False)
        repeated = RepeatTransaction()

                  


        if 'repeat' not in self.request.POST or transacao.total_repeats==0:
            transacao.repeat = False
            transacao.total_repeats = 0 
            repeated.manageRepeated(transacao.pk)
            

        elif transacao.repeat == False:
            transacao.repeat = True
            repeated.createRepeatedTransactions(transacao.total_repeats,
                                                transacao.data, 
                                                form.cleaned_data,
                                                self.request.user)
        else:
            if Transacoes.objects.get(pk=transacao.id) != transacao.data:
                repeated.manageRepeated(transacao.pk)
                repeated.createRepeatedTransactions(transacao.total_repeats,
                                                    transacao.data, 
                                                    form.cleaned_data,
                                                    self.request.user)

                repeated.manageRepeated(transacao.pk, update=form.cleaned_data)
                return super(TransacaoUpdate, self).form_valid(form)

            if Transacoes.objects.get(
                pk=transacao.pk).total_repeats != transacao.total_repeats:
                """Changing the number of repetitions, makes necessary
                to remove and recreate all the repetitions.
                """
                repeated.manageRepeated(transacao.pk)
                repeated.createRepeatedTransactions(transacao.total_repeats,
                                                    transacao.data, 
                                                    form.cleaned_data,
                                                    self.request.user)

            repeated.manageRepeated(transacao.pk, update=form.cleaned_data)

        return super(TransacaoUpdate, self).form_valid(form)

    #def form_invalid(self, form):


class TransacaoDelete(generic.edit.DeleteView):
    model = Transacoes
    success_url = '/menu/Transacoes'
    template_name = 'cadastro/confirm_delete.html'

    def post(self, request, **kwargs):
        if 'cancel' in request.POST:
            return redirect('/menu/Transacoes')
        else:
            try:
                repeated = RepeatTransaction()
                repeated.manageRepeated(kwargs.get('pk'))
                
                return super(TransacaoDelete, self).post(request, **kwargs)
            except ProtectedError:
                print('Adicionar Messagem informativa.')
                print(ProtectedError)
                #Adicionar template para mostrar erros
                #Recriar repetidos, caso o principal não seja excluído
                return redirect('/menu/Transacoes')

class LogoutView(generic.View):
    def get(self, request):
        logout(request)
        return redirect('/menu')



"""
TODO:
    Teste navigation at Year/Month menu.

   *Check query set in statistics, when retrieving future transacions.

    At future transactions, Fix the calculation for the paid documents:
        Must filter by 'gte' current_date or 'gt'

    "Navegue por datas" is not correctly ordered, test for years less than
        198.. change it to a OrderedDict

    Test: Create a Transacao with old date, then, update it to present date.
        Do the same with a Transacao which has repeated dates.

    Test when updating "data" attribute for transacoes.
        Test with repeated days.
        When creating a future date that has data greater than today's date,
        set repeat property to True???? (this will allow this to be shown as a 
        future Transacation.

    Add javascript validations to: If user selects "Repeat", 
        it must insert a value for total_repeats

    Create statistics based on the last three months:
        Sample: If a payment occurred at the same date for
        the last three months send mail or send message informing 
        that at this date you have this payment to do 

    Create Create user functionality at login template

    Change Login app name to account_hadling (this app will
    be responsible to login/out and create new users)

    Ao cadastrar uma transação, caso ocorram erros, a aplicação não 
        stá retornando um response, verificar (form_invalid) de 
        cadastro.views
        Tratar campo Valor do lado cliente, para trocar ',' por '.'usar replace.
        Ou verificar se existe algum campo para "currency" no html

    Criar template(Modal) para mostrar erros

    Criar app para lançar planejamento futuro

    Adicionar validação de usuário para cadastro de Transacoes (login required)

    Verificar formatação de campo html para campo valor monetário

"""
