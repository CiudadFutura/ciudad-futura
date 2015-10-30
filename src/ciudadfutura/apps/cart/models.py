from django.db import models
from ciudadfutura.apps.product.models import Product


class Cart(models.Model):

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

    def add_item(self, product_id, quantity):
        product = Product.objects.get(id=product_id)
        item, created = Item.objects.get_or_create(
            sku=product.sku, cart=self,
            price=product.price,
            market_price=product.market_price,
            name=product.name
        )
        if created:
            item.quantity = int(quantity)
        else:
            item.quantity += int(quantity)
        item.save(update_fields=['quantity'])

        return item

    def remove_item(self, item_id):
        print self.items.get(id=item_id).delete()


class Item(models.Model):

    sku = models.CharField(max_length=255, null=True, blank=False)
    name = models.CharField(max_length=255, null=True, blank=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    market_price = models.DecimalField(max_digits=8, decimal_places=2)
    cart = models.ForeignKey('ciudadfutura_cart.Cart', related_name='items')
    quantity = models.IntegerField(default=0)

    @property
    def total(self):
        return self.quantity * self.price
