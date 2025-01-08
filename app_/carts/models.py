from django.db import models

from goods.models import Products
from users.models import User

# Create your models here.

class CartQuerySet(models.QuerySet):

    def total_price(self):
        return sum([cart.product_price() for cart in self])

    def total_qty(self):
        if self:
            return sum([cart.qty for cart in self])

        return 0
    
class Cart(models.Model):

    user = models.ForeignKey(to= User, on_delete=models.CASCADE,blank=True, null=True, verbose_name='Пользователь')
    product = models.ForeignKey(to= Products, on_delete=models.CASCADE, verbose_name='Товар')
    qty = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    session_key = models.CharField(max_length=40, blank=True, null=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    class Meta:
        db_table = 'cart'
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    objects = CartQuerySet().as_manager()

    def product_price(self):
        return round(self.product.sell_price() * self.qty, 2)

    def __str__(self):
        return f'Корзина пользователя: {self.user.username} | Товар: {self.product.name} | Количество: {self.qty}'