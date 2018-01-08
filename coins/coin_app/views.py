from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
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
