# Software Development Cycle
## Restaurant Pancake

During the Expert Phase of my Secondary Education specializing in software development, I prepared for the exams. That´s what we actually do during the **Expert Phase**, preparing for exams.

I had the option to choose a project. I chose project **Restaurant Pancake**. As always my solution is to build a web application with Django. 

## About the project

For this project I needed to build a restaurant order system. If you have ever been in a restaurant where you can order food from your table using a tablet, that is exactly what I needed to build. 

## Project requirements

Below a list of the minimal requirements of this project.

- Order items from menu
- Calculate total price each time item is added
- See from which table an order had been made

For this project I knew I had to use Django's Session Framework. I had never worked with this, so I had to do some google magic to figure out how to use it. Eventually I found a great example inside the **Django by Example** book. 

Below the code I got from the book. I had to make some changes though.

```python
from decimal import Decimal
from django.conf import settings

from menu.models import MenuItem


class Cart:
    
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, menu_item, quantity=1, update_quantity=False):
        # Add a menu item to the cart or update its quantity
        menu_item_id = str(menu_item.id)

        if menu_item_id not in self.cart:
            self.cart[menu_item_id] = {'quantity': 0,
                                       'price': str(menu_item.price)}
        
        if update_quantity:
            self.cart[menu_item_id]['quantity'] = quantity
        else:
            self.cart[menu_item_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Mark the session as "modified" to make sure its saved
        self.session.modified = True

    def remove(self, menu_item):
        # Remove a product from the cart
        menu_item_id = str(menu_item.id)
        if menu_item_id in self.cart:
            del self.cart[menu_item_id]
            self.save()

    def __iter__(self):
        # Iterate over the item in the cart and get the products from the DB
        menu_item_ids = self.cart.keys()
        # get thte product objects and add them to the cart
        menu_items = MenuItem.objects.filter(id__in=menu_item_ids)
        
        for menu_item in menu_items:
            self.cart[str(menu_item.id)]['menu_item'] = menu_item

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        # Count all the items in the cart
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # Remove cart from the session
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
```
 
