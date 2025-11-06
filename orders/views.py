from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.db import transaction
from .models import OrderItem, Order
from shop.models import Product
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created_task


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                order = form.save(commit=False)
                if request.user.is_authenticated:
                    order.user = request.user
                order.save()

                for item in cart:
                    OrderItem.objects.create(order=order,
                                             product=item['product'],
                                             price=item['price'],
                                             quantity=item['quantity'])

                    product = item['product']
                    product.stock -= item['quantity']
                    product.save()

            cart.clear()
            order_created_task.delay(order.id)

            return redirect(reverse('orders:order_created', args=[order.id]))
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html',
                  {'cart': cart, 'form': form})


def order_created(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/created.html', {'order': order})