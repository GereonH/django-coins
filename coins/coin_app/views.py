from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView,FormView,RedirectView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from coin_app import models

class IndexView(TemplateView):
    template_name = 'coin_app/coin_index.html'

class CoinListView(ListView):
    model = models.Coin

class CoinDetailView(DetailView):
    context_object_name = 'coin_detail'
    model = models.Coin
    template_name = 'coin_app/coin_detail.html'

class CoinCreateView(CreateView):
    fields = ('coin_id',)
    model = models.Coin

class CoinUpdateView(UpdateView):
    fields = ('coin_id',)
    model = models.Coin

class CoinDeleteView(DeleteView):
    model = models.Coin
    success_url = reverse_lazy("coin_app:list")

@method_decorator(login_required, name='dispatch')
class HoldingsListView(ListView):
    model = models.Holdings

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

@method_decorator(login_required, name='dispatch')
class HoldingsCreateView(CreateView):
    fields = ('coin_id','amount','user',)
    model = models.Holdings

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
