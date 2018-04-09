from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from menu.models import MenuItem

from .cart import Cart
from .forms import AddMenuItemForm

@require_POST
def add_menu_item(request, id):
    cart = Cart(request)
    menu_item = get_object_or_404(MenuItem, id=id)
    form = AddMenuItemForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(menu_item=menu_item,
                quantity=cd['quantity'],
                update_quantity=cd['update'])
    return redirect('menu:list')

@login_required
def remove_menu_item(request, id):
    cart = Cart(request)
    menu_item = get_object_or_404(MenuItem, id=id)
    cart.remove(menu_item)
    return redirect('menu:list')


# def cart_detail(request):
#     cart = Cart(request)
#     context = {
#         'cart': cart
#     }
#     return render(request, 'cart/cart_detail.html', context)