from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext as _


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_staff = False
        user.is_admin = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_staff = True
        user.is_admin = False
        user.save(using=self._db)
        return user


class Person(models.Model):
    address = models.CharField(
        max_length=255, verbose_name=_('Address')
    )


class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    person = models.OneToOneField('ciudadfutura_auth.Person', null=True, default=None)

    objects = UserManager()

    def has_module_perms(self, module):
        return self.is_admin

    def has_perm(self, module):
        return self.is_admin

    def get_short_name(self):
        return self.name or self.email


class Profile(models.Model):

    class Meta:
        abstract = True


class Facebook(Profile):
    user = models.ForeignKey('ciudadfutura_auth.User', related_name='facebook')
    email = models.EmailField()
    token = models.TextField()


class Supplier(Profile):
    user = models.ForeignKey('ciudadfutura_auth.User', related_name='supplier')
    default_zones = models.ManyToManyField('ciudadfutura_product.Zone')

    def __str__(self):
        return self.user.name


class MisionMember(Profile):
    user = models.ForeignKey('ciudadfutura_auth.User', related_name='member')
    circle = models.ForeignKey('ciudadfutura_mision.Circle', null=True, blank=True)
    is_lead = models.BooleanField(default=False)
