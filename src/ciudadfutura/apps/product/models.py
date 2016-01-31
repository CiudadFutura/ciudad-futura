from django.db import models
from django.utils.translation import ugettext as _


class Zone(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Packaging(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class PriceChange(models.Model):
    product = models.ForeignKey('ciudadfutura_product.Product')
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    market_price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        ordering = ['-created_at']


class Product(models.Model):

    sku = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    max_allowed_per_user = models.IntegerField(default=1)
    price = models.FloatField()
    market_price = models.FloatField()
    image = models.FileField()
    supplier = models.ForeignKey('ciudadfutura_auth.Supplier')
    saleable = models.BooleanField(default=True)
    packaging = models.ForeignKey('ciudadfutura_product.Packaging')
    zones = models.ManyToManyField('ciudadfutura_product.Zone', blank=True)
    category = models.ManyToManyField('ciudadfutura_product.Category', verbose_name=_('Category'), blank=True)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def get_products(self):
        return Product.objects.filter(category=self)

