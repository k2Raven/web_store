from django.db import models


class Cart(models.Model):
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, related_name='cart_product',
                                verbose_name='Продукт')
    qty = models.PositiveIntegerField(verbose_name='Количество', default=0)

    def get_total(self):
        return self.product.price * self.qty
