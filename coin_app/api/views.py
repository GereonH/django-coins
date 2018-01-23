from django.db.models import Q
from rest_framework import generics, mixins

from coin_app.models import Coin
from .permissions import IsOwnerOrReadOnly
from .serializer import CoinSerializer

class CoinsAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field        = 'pk'
    serializer_class    = CoinSerializer
    #get_queryset        = Coin.objects.all()

    def get_queryset(self):
        qs = Coin.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(coin_id__icontains=query))
        return qs

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

    def post(self,request,*args,**kwargs):
        return self.create(request, *args,**kwargs)

class CoinsRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field        = 'pk'
    serializer_class    = CoinSerializer
    permission_classes  = [IsOwnerOrReadOnly]
    #get_queryset        = Coin.objects.all()

    def get_queryset(self):
        return Coin.objects.all()
    #
    # def perform_create(self,serializer):
    #     serializer.save(user=self.request.user)
