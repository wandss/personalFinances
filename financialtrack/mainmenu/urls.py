#*-* coding:utf-8 *-*
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from mainmenu.views import (MenuView, DespesasView, TransacoesView,
                            DespesaUpdate, DespesaDelete, TransacaoUpdate,
                            TransacaoDelete) 



urlpatterns = [
    url(r'^$', MenuView.as_view(), name='mainmenu'),
    url(r'^Despesas/$', login_required(DespesasView.as_view()),
        name='Despesas'),
    url(r'^Despesas/(?P<pk>[0-9]+)/$', DespesaUpdate.as_view(),
        name='despesa_update'),
    url(r'^Despesas/(?P<pk>[0-9]+)/delete/$', DespesaDelete.as_view(),
        name='despesa_delete'),
    url(r'^Transacoes/$', login_required(TransacoesView.as_view()),
        name='Transacoes'),
    url(r'^Transacoes/(?P<pk>[0-9]+)/$', login_required(
        TransacaoUpdate.as_view()), name='transacao_update'),
    url(r'^Transacoes/(?P<year>[0-9]+)/(?P<month>[0-9]+)/(?P<pk>[0-9]+)/$',
        login_required(TransacaoUpdate.as_view()), name='transacao_update'),
    url(r'^Transacoes/(?P<year>[0-9]+)/(?P<month>[0-9]+)/$', login_required(
        TransacoesView.as_view()), name='transacao'),
    url(r'^(?P<pk>[0-9]+)/delete/$', TransacaoDelete.as_view(), 
        name='transacao_delete'),
]

