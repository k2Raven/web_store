from django.db import models



class OrderProduct(models.Model):
    product = models.ForeignKey('webapp.Product', on_delete=models.RESTRICT, verbose_name='Продукт')
    order = models.ForeignKey('webapp.Order', on_delete=models.RESTRICT, verbose_name='Заказ')
    qty = models.PositiveIntegerField(verbose_name='Количество')

class Order(models.Model):
    username = models.CharField(max_length=100, verbose_name='Имя пользователя')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    address = models.CharField(max_length=500, verbose_name='Адрес')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создание')
    products = models.ManyToManyField('webapp.Product', related_name='orders', through=OrderProduct,
                                      through_fields=('order', 'product'), verbose_name='Товары' )
