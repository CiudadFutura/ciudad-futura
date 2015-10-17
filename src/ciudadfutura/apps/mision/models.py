from django.db import models


class Circle(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    shopping_cycle = models.ForeignKey('ciudadfutura_mision.ShoppingCycle', related_name='circles', null=True)


class ShoppingCycle(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    end_pay_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Invite(models.Model):
    email = models.EmailField(null=True, blank=False)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    circle = models.ForeignKey('ciudadfutura_mision.Circle', related_name='invites', null=True)
    activation_key = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
