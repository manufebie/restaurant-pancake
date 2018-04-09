from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class TableNumber(models.Model):
    '''
    One To One Relation with Django custom user model.
    The extension is used to add a table number for each table in the restaurant
    '''
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    table_number = models.PositiveIntegerField(null=True)

    class Meta:
        ordering = ['table_number',]

    def __str__(self):
        return str(self.table_number)

'''
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_table_number(sender, instance, created, **kwargs):
    if created:
        TableNumber.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_table_number_instance(sender, instance, **kwargs):
    instance.table_number.save()
'''

