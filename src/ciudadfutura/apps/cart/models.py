from django.db import models


class Cart(models.Model):

    def is_empty(self):
        return not bool(self.items.count())

    @property
    def total(self):
        return self.sub_total

    @property
    def sub_total(self):
        return sum([
            item.total for item in self.items.all()
        ])


class Item(models.Model):

    sku = models.CharField(max_length=255, null=True, blank=False)
    name = models.CharField(max_length=255, null=True, blank=False)
    price = models.FloatField()
    market_price = models.FloatField()
    cart = models.ForeignKey('ciudadfutura_cart.Cart', related_name='items')
    quantity = models.IntegerField(default=0)

    @property
    def total(self):
        return self.quantity * self.price
