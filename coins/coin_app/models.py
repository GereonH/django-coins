from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Coin(models.Model):
    coin_id = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.coin_id

    def get_absolute_url(self):
        return reverse("coin_app:detail",kwargs={'pk':self.pk})

class Exchange(models.Model):
    exchange_name = models.CharField(max_length=256)

    def __str__(self):
        return self.exchange_name


class Holdings(models.Model):
    CURRENCY_CHOICES = (
        ('EUR', 'EUR (€)'),
        ('USD', 'USD($)'),
    )

    coin_id = models.ForeignKey(Coin, on_delete=models.CASCADE, blank=True)
    amount = models.DecimalField(max_digits=60, decimal_places=10)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='EUR')
    user = models.ForeignKey(User, default='')
