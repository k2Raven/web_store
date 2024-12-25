from django.shortcuts import redirect
from django.views.generic import View

from webapp.forms import OrderForm
from webapp.models import Cart, OrderProduct


class OrderCreateView(View):
    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        cart_products = Cart.objects.all()
        if form.is_valid() and cart_products:
            order = form.save()
            for item in cart_products:
                item.product.qty -= item.qty
                item.product.save()
                OrderProduct.objects.create(order=order, product=item.product, qty=item.qty)
                item.delete()
        return redirect('product-list')