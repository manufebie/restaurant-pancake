from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save

from base.utils import unique_order_id_generator
from menu.models import MenuItem


class Order(models.Model):
    STATUS_CHOICES = (
        ('in behandeling', 'In behandeling'),
        ('klaar', 'Klaar')
    )
    # random_id = models.CharField(max_length=255)
    table = models.ForeignKey(settings.AUTH_USER_MODEL)
    item = models.ForeignKey(MenuItem, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='in behandeling')
    paid = models.BooleanField(default=False)

    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp',]

    def __str__(self):
        return '{}'.format(self.id)

    def get_total_cost(self):
        return self.price * self.quantity