from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, UpdateView

from .forms import OrderDoneForm
from .models import Order
from cart.cart import Cart

@login_required
def create_order(request):
    cart = Cart(request)
    
    if request.method == 'POST':
        for item in cart:
            Order.objects.create(table=request.user,
                                 item=item['menu_item'],
                                 price=item['price'],
                                 quantity=item['quantity'])
        cart.clear()
        return render(request, 'orders/order_success.html', {'cart': cart})
    
    return render(request, 'cart/cart_detail.html', {'cart': cart})


# Class Based Views

class OrderListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Order
    permission_required = 'staff_member'
    
    