import random
import string

from django.utils.text import slugify

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_order_id_generator(instance):
    random_order_id = random_string_generator().upper()

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(order_id=random_order_id).exists()
    if qs_exists:
        return unique_order_id_generator(instance)
    return random_order_id