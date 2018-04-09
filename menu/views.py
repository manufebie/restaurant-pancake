from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Category, MenuItem

from cart.cart import Cart
from cart.forms import AddMenuItemForm

@login_required
def menu_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    items = MenuItem.objects.filter(available=True)
    form = AddMenuItemForm()
    cart = Cart(request)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        items = items.filter(category=category)
    

    context = {'category': category,
               'categories': categories,
               'items': items,
               'form': form,
               'cart': cart}
    return render(request, 'menu/menuitem_list.html', context)

@login_required
def menu_item_detail(request, id):
    item = get_object_or_404(MenuItem,
                             id=id,
                             available=True)
    context = {
        'item': item
    }

    return render(request, 'menu/item_detail.html', context)