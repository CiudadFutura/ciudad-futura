from django.db import models
from django.utils.translation import ugettext_lazy as _
from ciudadfutura.apps.cart.models import Cart


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

STATUS_ITEMS_CHOICES = (
    ('added', _('Added')),
    ('deleted', _('Deleted'))
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
            i.qty for i in self.items.all()
        ])

    @property
    def sub_total(self):
        return sum([
            item.total for item in self.items.all()
        ])

    @property
    def market_sub_total(self):
        return sum([
            item.total_market for item in self.items.all()
        ])

    @property
    def purchase_saving(self):
        return (1 - self.sub_total / self.market_sub_total) * 100

    def add_item(self, cart_id):
        cart = Cart.objects.get(id=cart_id)
        for i in cart.items.all():
            item, created = OrderItem.objects.get_or_create(
                product_sku=i.sku,
                order=self,
                product_price=i.price,
                product_market_price=i.market_price,
                product_name=i.name,
                product_real_price=i.price,
                product_description=i.description,
                qty=i.quantity
            )
            if created:
                item.qty = int(i.quantity)
            else:
                item.qty += int(i.quantity)
            item.save(update_fields=['qty'])

        return item

    def remove_item(self, item_id):
        print self.items.get(id=item_id).delete()

    reference = models.CharField(max_length=9)
    user = models.ForeignKey('ciudadfutura_auth.User', related_name='orders')
    shopping_cycle = models.ForeignKey('ciudadfutura_mision.ShoppingCycle', related_name='cycles', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderItem(models.Model):

    @property
    def total(self):
        return self.qty * self.product_price

    @property
    def total_market(self):
        return self.qty * self.product_market_price

    STATUS_CHOICES = STATUS_ITEMS_CHOICES
    status = models.CharField(
        max_length=32,
        choices=STATUS_CHOICES,
        default='added'
    )

    order = models.ForeignKey('ciudadfutura_order.Order', related_name='items')
    supplier = models.ForeignKey('ciudadfutura_auth.Supplier', related_name='suppliers', null=True)
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

    STATUS_CHOICES = STATUS_CHOICES

    status = models.CharField(
        max_length=32,
        choices=STATUS_CHOICES,
        default='new'
    )

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
    def total(self):
        return self.qty * self.product_price

    @property
    def total_market(self):
        return self.quantity * self.product_market_price

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
