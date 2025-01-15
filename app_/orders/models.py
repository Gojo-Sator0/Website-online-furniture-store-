from django.db import models
from goods.models import Products
from users.models import User

# Create your models here.

class OrderitemQuerySet(models.QuerySet):
    def total_price(self):
        return sum(cart.products_price() for cart in self)
    
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, verbose_name='Пользователь', default=None, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    requires_delivery = models.BooleanField(default=True, verbose_name='Требуется доставка')
    delivery_address = models.TextField(null=True, blank=True, verbose_name='Адрес доставки')
    payment_on_get = models.BooleanField(default=True, verbose_name='Оплата при получении')
    is_paid = models.BooleanField(default=False, verbose_name='Оплачен')
    status = models.CharField(max_length=100, verbose_name='Статус заказа', default='В обработке')

    class Meta:
        db_table = 'order'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ №{self.pk} | Покупатель: {self.user} | Статус: {self.status}'
    
class Orderitem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Products, on_delete=models.SET_DEFAULT, verbose_name='Товар', default=0, null=True, blank=True)
    name = models.CharField(max_length=255, verbose_name='Название')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    
    class Meta:
        db_table = 'order_item'
        verbose_name = 'Проданный товар'
        verbose_name_plural = 'Проданные товары'

    objects = OrderitemQuerySet.as_manager()

    def products_price(self):
        return round(self.price() * self.quantity, 2)
    
    def __str__(self):
        return f'Товар: {self.name} | Заказ №{self.order.pk}'
    
