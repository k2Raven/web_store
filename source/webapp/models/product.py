from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    category = models.ForeignKey('webapp.Category', on_delete=models.RESTRICT, related_name='products', verbose_name='Категория')
    price = models.DecimalField( max_digits=12, decimal_places=2,verbose_name='Стоимость')
    picture = models.URLField(verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создание')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')


    def __str__(self):
        return f'{self.name} ({self.id})'

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
