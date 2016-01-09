from django.db import models
from django.utils.translation import ugettext_lazy as _
from ciudadfutura.apps.product.models import Product


STATUS_CHOICES = (
    ('new', _('New order')),
    ('canceled', _('Canceled')),
    ('on_hold', _('On hold')),
    ('pending_payment', _('Pending payment')),
    ('pending_received', _('Pending received')),
    ('shipped', _('Order shipped')),
    ('paid', _('Paid')),
    ('closed', _('Closed')),
)


class Order(models.Model):

    STATUS_CHOICES = STATUS_CHOICES
    status = models.CharField(
        max_length=32,
        choices=STATUS_CHOICES,
        default='new'
    )

    def is_empty(self):
        return not bool(self.items.count())

    @property
    def total(self):
        return self.sub_total

    @property
    def total_items(self):
        return sum([
            i.quantity for i in self.items.all()
        ])

    @property
    def sub_total(self):
        return sum([
            item.total for item in self.items.all()
        ])

    def add_item(self, product_sku, quantity, price, market_price):
        product = Product.objects.get(sku=product_sku)
        item, created = OrderItem.objects.get_or_create(
            product_sku=product.sku,
            order=self,
            product_price=price,
            product_market_price=market_price,
            product_name=product.name,
            product_real_price=price,
            product=product,
            product_description=product.description,
            qty=quantity
        )
        if created:
            item.qty = int(quantity)
        else:
            item.qty += int(quantity)
        item.save(update_fields=['qty'])

        return item

    def remove_item(self, item_id):
        print self.items.get(id=item_id).delete()

    reference = models.CharField(max_length=9)
    total = models.DecimalField(max_digits=8, decimal_places=2, default=0)
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
