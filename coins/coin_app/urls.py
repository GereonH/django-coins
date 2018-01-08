from django.conf.urls import url
from coin_app import views

app_name = 'coin_app'

urlpatterns = [
    url(r'^coins/$', views.CoinListView.as_view(),name="list"),
    url(r'^$', views.IndexView.as_view(),name="index"),
    url(r'^coins/(?P<pk>\d+)/$',views.CoinDetailView.as_view(), name='detail'),
    url(r'^coins/create_coin/$',views.CoinCreateView.as_view(), name="create"),
    url(r'^coins/update/(?P<pk>\d+)/$',views.CoinUpdateView.as_view(), name='update'),
    url(r'^coins/delete/(?P<pk>\d+)/$',views.CoinDeleteView.as_view(), name='delete'),
]
