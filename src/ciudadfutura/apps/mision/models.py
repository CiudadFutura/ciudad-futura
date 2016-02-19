from django.db import models
from datetime import datetime, timedelta, time


class Circle(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    shopping_cycle = models.ForeignKey('ciudadfutura_mision.ShoppingCycle', related_name='circles', null=True)


class ShoppingCycleQuerySet(models.QuerySet):

    def current_cycle(self):
        today = datetime.now().date()
        return self.filter(start_date__lte=today,
                           delivery_date__gte=today
                           )

    def active(self):
        today = datetime.now().date()
        return self.filter(start_date__lte=today,
                           end_date__gte=today
                           )


class ShoppingCycleManager(models.Manager):

    def get_queryset(self):
        return ShoppingCycleQuerySet(self.model, using=self._db)

    def current_cycle(self):
        return self.get_queryset().current_cycle()


class ShoppingCycle(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    end_pay_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShoppingCycleManager()

    def __str__(self):
        return self.name


class Invite(models.Model):
    code = models.CharField(unique=True, max_length=255)
    email = models.EmailField(null=True, blank=False)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    circle = models.ForeignKey('ciudadfutura_mision.Circle', related_name='invites', null=True)
    activation_key = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




