from django.db.models import Sum, F
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DeleteView, View
from django.urls import reverse, reverse_lazy
from webapp.forms import CartFrom
from webapp.models import Cart, Product


class CartView(ListView):
    model = Cart
    context_object_name = 'cart_products'
    template_name = 'cart/cart_list.html'

    def get_context_data( self, **kwargs ):
        context = super().get_context_data(**kwargs)
        context['cart_total'] = self.object_list.aggregate(total=Sum(F('product__price') * F('qty') ))['total']
        return context

class ProductsAddToCartView(View):

    def post(self, request, pk, *args, **kwargs):
        product = get_object_or_404(Product, pk=pk)
        qty = float(request.POST.get('qty', 0))
        next_url = request.GET.get('next', 'product-list')
        if product.qty > 0 and qty > 0:
            cart, is_created = Cart.objects.get_or_create(product=product)
            if cart.qty + qty <= product.qty:
                cart.qty += qty
                cart.save()
        return redirect(next_url)


class ProductsRemoveFromCartView(DeleteView):
    model = Cart
    success_url = reverse_lazy('cart_list')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class ProductsRemoveFromCartPieceByPieceView(View):
    def get(self, request, *args, **kwargs):
        cart = get_object_or_404(Cart, pk=self.kwargs['pk'])
        if cart.qty == 1:
            cart.delete()
        else:
            cart.qty -= 1
            cart.save()
        return redirect('cart_list')



