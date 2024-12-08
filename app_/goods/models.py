from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Названия')
    slug = models.SlugField(max_length=160, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    

class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Названия')
    slug = models.SlugField(max_length=160, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описания')
    image = models.ImageField(upload_to='goods_img',blank=True, null=True, verbose_name='Изоражения')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ("id",)
    
    def display_id(self):
        return f"{self.id:05}" #добавления нулей в id
    
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount/100, 2)
        
        return self.price
