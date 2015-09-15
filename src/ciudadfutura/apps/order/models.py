from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


STATUS_CHOICES = (
    ('canceled', _('Canceled')),
    ('STATUS2', _('Status #2')),
    ('STATUS3', _('Status #1')),
)


class Order(models.Model):

    STATUS_CHOICES = STATUS_CHOICES
    status = models.CharField(
        max_length=32,
        choices=STATUS_CHOICES,
        default='open'
    )

    reference = models.CharField(max_length=9)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey('ciudadfutura_auth.User', related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderItem(models.Model):

    @property
    def row_total(self):
        return self.qty * self.product_price

    order = models.ForeignKey('ciudadfutura_order.Order', related_name='items')

    product = models.ForeignKey('ciudadfutura_product.Product', related_name='orders_items')
    product_name = models.CharField(max_length=255)
    product_sku = models.CharField(max_length=255)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=8, decimal_places=2)
    product_real_price = models.DecimalField(max_digits=8, decimal_places=2)
    product_market_price = models.DecimalField(max_digits=8, decimal_places=2)
    qty = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Invoice(models.Model):

    number = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    order = models.ForeignKey('ciudadfutura_order.Order', related_name='invoices')
    user = models.ForeignKey('ciudadfutura_auth.User', related_name='invoices')
    user_first_name = models.CharField(max_length=255)
    user_second_name = models.CharField(max_length=255)
    user_address = models.CharField(max_length=255)
    type = models.CharField(max_length=1)
    note = models.TextField()
    # transaction = models.ForeignKey('ciudadfutura_transaction.Transaction', related_name='transaction')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class InvoiceItem(models.Model):

    @property
    def row_total(self):
        return self.qty * self.product_price

    invoice = models.ForeignKey('ciudadfutura_order.Invoice', related_name='items')
    product = models.ForeignKey('ciudadfutura_product.Product', related_name='invoices_items')
    product_name = models.CharField(max_length=255)
    product_sku = models.CharField(max_length=255)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=8, decimal_places=2)
    product_real_price = models.DecimalField(max_digits=8, decimal_places=2)
    product_market_price = models.DecimalField(max_digits=8, decimal_places=2)
    qty = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
