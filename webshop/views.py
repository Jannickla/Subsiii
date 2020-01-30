from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Box, Order, OrderItem, OrderBox
from django.utils import timezone
from django.views.generic import ListView, DetailView


def shop_home(request):
    context = {
        'title': 'Welcome to the worlds easiest subscription platform',
        'bodyClass': 'homePage',
        'box': Box.objects.all(),
    }
    return render(request, 'index.html', context)


def shop_about(request):
    context = {
        'title': 'About us and our mission',
        'bodyClass': 'aboutPage',
    }
    return render(request, 'about.html', context)


class BoxDetailView(DetailView):
    model = Box
    template_name = 'box.html'


def shop_cart(DetailView):
    model = Order
    context = {
        'title': 'Your Cart',
        'bodyClass': 'productCart',
    }



def shop_checkout(request):
    context = {
        'title': 'Payment',
        'bodyClass': 'productCheckout',
    }
    return render(request, 'checkout.html', context)


def shop_register(request):
    context = {
        'title': 'Payment',
        'bodyClass': 'productregister',
    }
    return render(request, 'index.html', context)


class BoxShopView(ListView):
    model = Box
    context = {
        'title': 'Boxes',
        'bodyClass': 'productBoxes',
    }
    paginate_by = 3
    template_name = 'boxes.html'


def add_to_cart(request, slug):

    # Get the item from the slug via get_object_or_404 method
    box = get_object_or_404(Box, slug=slug)
    # Check if the user have an order
    order_box, created = OrderBox.objects.get_or_create(
        box=box,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        # Check if order item is in the order
        if order.box.filter(box__slug=box.slug).exists():
            order_box.quantity += 1
            order_box.save()
            messages.info(request, 'The quantity was updated')
            return redirect('webshop:shop-cart')
        else:
            messages.info(request, 'This box was added')
            order.box.add(order_box)
            return redirect('webshop:shop-cart')
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.box.add(order_box)
        messages.info(request, 'This box was added')
        return redirect('webshop:shop-cart')


def remove_from_cart(request, slug):

    # Get the item from the slug via get_object_or_404 method
    box = get_object_or_404(Box, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        # Check if order item is in the order
        if order.box.filter(box__slug=box.slug).exists():
            order_box = OrderBox.objects.filter(
                box=box,
                user=request.user,
                ordered=False
            )[0]
            order.box.remove(order_box)
            messages.info(request, 'This box was removed')
            return redirect('webshop:shop-cart', slug=slug)
        else:
            messages.info(request, 'This box was not in your cart')
            return redirect('webshop:shop-cart', slug=slug)
    else:
        messages.info(request, 'You do not have an active order')
        return redirect('webshop:shop-cart', slug=slug)
