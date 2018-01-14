from rest_framework import serializers
from coin_app.models import Coin

class CoinSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coin
        fields = [
            'pk',
            'coin_id',
        ]

    def validate_coin_id(self,value):
        qs = Coin.objects.filter(coin_id__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("The coin id must be unique")
        return value
