from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name} ({self.id})'

    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
