from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from cadastro.views import CadastroView, DespesaCreate, TransacoesCreate

urlpatterns = [
    url(r'^$', CadastroView.as_view(), name="cadastro"),
    url(r'^Despesas/add/$', login_required(DespesaCreate.as_view()), 
        name="despesa_add"),
    url(r'^Transacoes/add/$', login_required(TransacoesCreate.as_view()),
        name="transacoes_add"),
]
