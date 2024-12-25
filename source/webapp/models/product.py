from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    category = models.ForeignKey('webapp.Category', on_delete=models.RESTRICT, related_name='products', verbose_name='Категория')
    price = models.DecimalField( max_digits=7, decimal_places=2, validators=[MinValueValidator(0)], verbose_name='Стоимость')
    picture = models.URLField(verbose_name='Изображение')
    qty = models.PositiveIntegerField(verbose_name='Остаток', default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создание')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.name} ({self.id})'

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
