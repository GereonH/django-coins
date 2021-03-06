from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from coin_app import models
from coin_app.models import Coin,Holdings,Exchange
from coin_app.templatetags import cmc_logger
import requests

class IndexView(generic.TemplateView):
    template_name = 'coin_app/coin_index.html'

class CoinListView(generic.ListView):
    model = models.Coin

    def get_queryset(self):
        return Coin.objects.order_by('id')


class CoinDetailView(generic.DetailView):
    context_object_name = 'coin_detail'
    model = models.Coin

class CoinCreateView(generic.CreateView):
    fields = ('coin_id',)
    model = models.Coin

class CoinUpdateView(generic.UpdateView):
    fields = ('coin_id',)
    model = models.Coin

class CoinDeleteView(generic.DeleteView):
    model = models.Coin
    success_url = reverse_lazy("coin_app:list")

@method_decorator(login_required, name='dispatch')
class HoldingsMutipleModelView(generic.TemplateView):
    model = models.Holdings
    template_name = 'coin_app/holdings_list.html'

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(HoldingsMutipleModelView, self).get_context_data(**kwargs)
        context['coin']     = Coin.objects.all()
        context['exchange'] = Exchange.objects.all()
        context['holdings'] = Holdings.objects.filter(user=self.request.user)
        return context


@method_decorator(login_required, name='dispatch')
class HoldingsCreateView(generic.CreateView):
    fields = ('coin_id', 'exchange' ,'amount','user', )
    model = models.Holdings
    success_url = reverse_lazy("coin_app:holdings")

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

@method_decorator(login_required, name='dispatch')
class HoldingsDetailView(generic.DetailView):
    context_object_name = 'holdings_detail'
    model = models.Holdings
    template_name = 'coin_app/holdings_detail.html'

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

@method_decorator(login_required, name='dispatch')
class HoldingsUpdateView(generic.UpdateView):
    fields = ('amount',)
    model = models.Holdings

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class BinanceAPIView(generic.TemplateView):
    template_name='coin_app/binance.html'

class NewCoinsView(generic.TemplateView):
    template_name='coin_app/newcoins.html'

    def gather_data(self):

        # get top 10 coins in a list
        r = requests.get('https://api.coinmarketcap.com/v1/ticker/?limit=10', params=None)
        return r.json()

    def gather_image(self,coin_id):
        img_url = 'https://files.coinmarketcap.com/static/img/coins/128x128/'+id+'.png'
        return img_url


    # def testing(self):
    #     summ = 1+1
    #     return summ
    #
    # def etherparty(self):
    #     fuel = cmc_logger.get_json_by_id('etherparty','rank')
    #     return fuel
