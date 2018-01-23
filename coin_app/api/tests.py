from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

from coin_app.models import Coin
User = get_user_model()


class CoinAPITestCase(APITestCase):

    def setUp(self):
        user_obj = User(username='testuser', email='test@test.com')
        user_obj.set_password("testpassword1234")
        user_obj.save()
        coin = Coin.objects.create(
                        coin_id='new test coin'
                        )

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_coin(self):
        coin_count = Coin.objects.count()
        self.assertEqual(coin_count, 1)
