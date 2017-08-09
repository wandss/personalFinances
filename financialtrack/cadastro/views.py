from django.views import generic
from .models import TipoDespesa, Transacoes
from mainmenu.models import MainMenu
from .choices import tipo_choices
from .repeatDates import RepeatTransaction

class CadastroView(generic.base.TemplateView):
    template_name = 'cadastro_view.html'

    def get_context_data(self, **kwargs):
        context = super(CadastroView, self).get_context_data(**kwargs)
        context['opcoes'] = MainMenu.objects.all()
        context['page_title'] = "Criar Registros"
        return context


class DespesaCreate(generic.edit.CreateView):
    model = TipoDespesa
    fields = ['nome']
    success_url = '/menu/Despesas/'


    def get_context_data(self, **kwargs):
        context = super(DespesaCreate, self).get_context_data(**kwargs)
        context['page_title'] = 'Adicionar Tipo de Despesa'
        return context

    def form_valid(self, form):
        tipo_despesa = form.save(commit=False)
        tipo_despesa.incluido_por = self.request.user
        return super(DespesaCreate, self).form_valid(form)
        


class TransacoesCreate(generic.edit.CreateView):
    model = Transacoes
    fields = ['estabelecimento','despesa','tipo_trans','valor','informacoes']
    success_url = '/menu/Transacoes/'

    def get_context_data(self, **kwargs):
        fields = [campos for campos in vars(Transacoes()).keys() 
                if '_' not in campos]
        context = super(TransacoesCreate, self).get_context_data(**kwargs)
        context['page_title'] = 'Adicionar Transação'
        context['campos'] = fields
        context['tipo_trans'] = tipo_choices
        context['despesas'] = TipoDespesa.objects.filter(
            incluido_por=self.request.user)
        return context

    def form_valid(self, form):
        transacao = form.save(commit=False)
        transacao.despesa = TipoDespesa.objects.get(
            pk=int(self.request.POST.get('despesa')))
        transacao.incluido_por = self.request.user
        if self.request.POST.get('data'):
            transacao.data = transacao.data.replace(
                year=int(self.request.POST.get('data').split('/')[-1]),
                month=int(self.request.POST.get('data').split('/')[1]),
                day=int(self.request.POST.get('data').split('/')[0]),
                hour=7, minute=40)

        if 'repeat' in self.request.POST:
           total_repeats = int(self.request.POST.get('total_repeats'))
           transacao.repeat = True
           transacao.total_repeats = total_repeats
           repeat = RepeatTransaction()
           repeat.createRepeatedTransactions(total_repeats, transacao.data,
                   form.cleaned_data, self.request.user)

        return super(TransacoesCreate, self).form_valid(form)
