from django.db import models


class Circle(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active_cycle = models.ForeignKey('ciudadfutura_mision.Cycle', related_name='circles', null=True)


class Cycle(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    end_pay_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
