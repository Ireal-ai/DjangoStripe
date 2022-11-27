from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class ItemModel(models.Model):
    name = models.CharField(max_length=70, verbose_name=_('Name'))
    description = models.TextField(verbose_name=_('Description'), max_length=1000)
    price = models.DecimalField(verbose_name=_('Price'), max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = _('item')
        verbose_name_plural = _('items')
