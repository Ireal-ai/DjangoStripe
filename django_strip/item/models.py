from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=70, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'), max_length=1000)
    price = models.DecimalField(verbose_name=_('Price'), max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = _('item')
        verbose_name_plural = _('items')


class Order(models.Model):

    id = models.BigAutoField(
        primary_key=True
    )

    # You can change as a Foreign Key to the user model
    customer_email = models.EmailField(
        verbose_name='Customer Email'
    )

    product = models.ForeignKey(
        to=Item,
        verbose_name='item',
        on_delete=models.PROTECT
    )

    amount = models.IntegerField(
        verbose_name='Amount'
    )

    stripe_payment_intent = models.CharField(
        max_length=200
    )

    # This field can be changed as status
    has_paid = models.BooleanField(
        default=False,
        verbose_name='Payment Status'
    )

    created_on = models.DateTimeField(
        auto_now_add=True
    )

    updated_on = models.DateTimeField(
        auto_now_add=True
    )
