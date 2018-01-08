from django.contrib import admin
from coin_app.models import Coin,Exchange,Holdings

# Register your models here.
admin.site.register(Coin)
admin.site.register(Exchange)
admin.site.register(Holdings)
