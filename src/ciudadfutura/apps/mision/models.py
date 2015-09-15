from django.db import models


class Circle(models.Model):

    user = models.ForeignKey('ciudadfutura_auth.User', related_name='leader')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Cycle(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    end_pay_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    circle = models.ForeignKey('ciudadfutura_mision.Circle', related_name='circles')
