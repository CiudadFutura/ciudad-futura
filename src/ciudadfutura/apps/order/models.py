from django.db import models
from django.utils import timezone


class AutoDateTimeField(models.DateTimeField):

    def pre_save(self, model_instance, add):
        return timezone.datetime.now()


class Order(models.Model):

    reference = models.CharField(max_length=9)
    status = models.CharField(max_length=32)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    invoice = models.CharField(max_digits=255)
    user = models.ForeignKey('ciudadfutura_auth.User', related_name='user')
    create_at = models.DateField(default=timezone.now)
    update_at = models.AutoDateTimeField(default=timezone.now)


class OrderItem(models.Model):

    def _get_row_total(self):
        return self.qty * self.product_price

    order = models.ForeignKey('ciudadfutura_order.Order', related_name='order')

    product = models.ForeignKey('ciudadfutura_product.Product', related_name='product')
    product_name = models.CharField(max_length=255)
    product_sku = models.CharField(max_length=255)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=8, decimal_places=2)
    product_real_price = models.DecimalField(max_digits=8, decimal_places=2)
    product_market_price = models.DecimalField(max_digits=8, decimal_places=2)
    qty = models.IntegerField()
    row_total = property(_get_row_total())
    create_at = models.DateField(default=timezone.now)
    update_at = models.AutoDateTimeField(default=timezone.now)
