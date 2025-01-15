from django.db.models import Sum, F
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, CreateView, DeleteView, View
from django.urls import reverse, reverse_lazy
from webapp.forms import CartFrom, OrderForm
from webapp.models import Cart, Product


class CartView(TemplateView):
    template_name = 'cart/cart_list.html'

    def get_context_data( self, **kwargs ):
        context = super().get_context_data(**kwargs)
        cart = self.request.session.get('cart', {})

        cart_total = 0
        products = Product.objects.filter(id__in=cart.keys())
        cart_products = []
        for product in products:
            qty = int(cart[str(product.id)])
            total = product.price * qty
            cart_total += total
            cart_products.append({'pk': product.id,'name': product.name, 'price': product.price, "qty": qty, 'total': total })
        context['cart_products'] = cart_products
        context['cart_total'] = cart_total
        context['form'] = OrderForm()
        return context

class ProductsAddToCartView(View):

    def post(self, request, pk, *args, **kwargs):
        product = get_object_or_404(Product, pk=pk)
        qty = int(request.POST.get('qty', 0))
        next_url = request.GET.get('next', 'product-list')
        cart = request.session.get('cart', {})
        print(cart)
        #{'1':3, '3':1 }
        if str(product.id) in cart:
            qty += cart[str(product.id)]

        if product.qty >= qty:
            cart[str(product.id)] = qty

        request.session['cart'] = cart
        # if product.qty > 0 and qty > 0:
        #     cart, is_created = Cart.objects.get_or_create(product=product)
        #     if cart.qty + qty <= product.qty:
        #         cart.qty += qty
        #         cart.save()
        return redirect(next_url)


class ProductsRemoveFromCartView(View):
    def get(self, request, pk,  *args, **kwargs):
        cart = request.session.get('cart', {})
        if str(pk) in cart:
            cart.pop(str(pk))
        request.session['cart'] = cart
        return redirect('cart_list')


class ProductsRemoveFromCartPieceByPieceView(View):
    def get(self, request, pk, *args, **kwargs):
        cart = request.session.get('cart', {})
        if str(pk) in cart:
            if cart[str(pk)] == 1:
                cart.pop(str(pk))
            else:
                cart[str(pk)] -= 1
        request.session['cart'] = cart
        return redirect('cart_list')



