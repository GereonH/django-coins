from django.conf.urls import url
from coin_app import views


app_name = 'coin_app'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(),name="index"),
    url(r'^coins/$', views.CoinListView.as_view(),name="list"),
    url(r'^coins/(?P<pk>\d+)/$',views.CoinDetailView.as_view(), name="detail"),
    url(r'^coins/create_coin/$',views.CoinCreateView.as_view(), name="create"),
    url(r'^coins/update/(?P<pk>\d+)/$',views.CoinUpdateView.as_view(), name="update"),
    url(r'^coins/delete/(?P<pk>\d+)/$',views.CoinDeleteView.as_view(), name="delete"),
    url(r'^holdings/$', views.HoldingsMutipleModelView.as_view(), name="holdings"),
    url(r'^holdings/create/$', views.HoldingsCreateView.as_view(), name="holdings_create"),
    url(r'^holdings/update/(?P<pk>\d+)/$',views.HoldingsUpdateView.as_view(), name="holdings_update"),
    url(r'^holdings/(?P<pk>\d+)/$',views.HoldingsDetailView.as_view(), name="holdings_detail"),
    url(r'^newcoins/$', views.NewCoinsView.as_view(), name="newcoins"),
    url(r'^binance/$', views.BinanceAPIView.as_view(), name="binance"),

]
