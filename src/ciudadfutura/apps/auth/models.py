from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


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
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    dni = models.IntegerField()
    birth_date = models.DateField()
    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=9)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    telephone = models.CharField(max_length=32)
    cellphone = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('ciudadfutura_auth.Tag')


class User(AbstractBaseUser):

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    reset_password_token = models.CharField()
    reset_password_sent_at = models.DateTimeField()
    confirmed_at = models.DateTimeField()
    confirmation_token = models.CharField()
    confirmation_sent_at = models.DateTimeField()
    unconfirmed_email = models.CharField()
    sign_in_count = models.IntegerField()
    current_sign_in_at = models.DateTimeField()
    last_sign_in_at = models.DateTimeField()
    current_sign_in_ip = models.CharField()
    last_sign_in_ip = models.CharField()

    USERNAME_FIELD = 'email'

    person = models.OneToOneField('ciudadfutura_auth.Person', null=True, default=None)

    objects = UserManager()

    def has_module_perms(self, module):
        return self.is_admin

    def has_perm(self, module):
        return self.is_admin

    def get_short_name(self):
        return self.name or self.email


class Tag(models.Model):
    name = models.CharField(max_length=255)


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
    circle = models.ForeignKey('ciudadfutura_mision.Circle', related_name='circles')
    is_lead = models.BooleanField(default=False)
