from django.db import models


class Circle(models.Model):

    def __str__(self):
        return 'Circle id: %s' % self.id
