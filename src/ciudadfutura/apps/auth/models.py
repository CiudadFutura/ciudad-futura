from uuid import uuid1 as generate_unique_username
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext as _
from django.db.models.signals import pre_save


class UserManager(BaseUserManager):

    def create_user(self, username, password, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.is_staff = False
        user.is_admin = False
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, password, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.is_staff = True
        user.is_admin = False
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    # General info
    dni = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    postal_code = models.CharField(max_length=9, null=True, blank=True)
    telephone = models.CharField(max_length=32, null=True, blank=True)
    cellphone = models.CharField(max_length=32, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, default='AR')
    avatar = models.ImageField('profile picture', upload_to='user/avatars', null=True, blank=True)
    address = models.CharField(
        max_length=255, verbose_name=_('Address'), null=True, blank=True
    )

    # Taxonomy
    contribution = models.TextField(
        verbose_name=_('Contribution'), null=True, blank=True
    )
    tags = models.ManyToManyField(
        'ciudadfutura_auth.Tag', verbose_name=_('Tags'), blank=True
    )
    relationships = models.ManyToManyField(
        'ciudadfutura_auth.Relationship',
        verbose_name=_('Relationships'),
        blank=True
    )

    # Authentication
    username = models.CharField(unique=True, max_length=255)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    # Changes tracking
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    # Legacy data from old database (serialized as json)
    legacy = models.TextField()

    USERNAME_FIELD = 'username'

    # Relationship Ids
    CIUDADANO = 1
    MISION = 2
    D7 = 3
    AFILIADO = 4

    objects = UserManager()

    @property
    def full_name(self):
        return ', '.join([
            n for n in [self.last_name, self.first_name] if n
        ]) or None

    # Alias
    name = full_name

    @property
    def has_relation(self):
        relationships = [
            r.id for r in self.relationships.all()
        ]
        return type('Relations', (object, ), {
            'CIUDADANO': 1 in relationships,
            'MISION': 2 in relationships,
            'D7': 3 in relationships,
            'AFILIADO': 4 in relationships,
        })()

    def has_module_perms(self, module):
        return self.is_admin

    def has_perm(self, module):
        return self.is_admin

    def get_short_name(self):
        return self.first_name or self.email

    def set_avatar(self):
        _avatar = self.avatar
        if not _avatar:
            self.avatar="avatar.png"


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Relationship(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Profile(models.Model):

    class Meta:
        abstract = True


class Facebook(Profile):
    user = models.OneToOneField('ciudadfutura_auth.User', related_name='facebook')
    email = models.EmailField()
    token = models.TextField()


class Supplier(Profile):
    user = models.OneToOneField('ciudadfutura_auth.User', related_name='supplier')
    default_zones = models.ManyToManyField('ciudadfutura_product.Zone')

    def __str__(self):
        return self.user.name


class MisionMember(Profile):
    user = models.OneToOneField('ciudadfutura_auth.User', related_name='member')
    circle = models.ForeignKey(
        'ciudadfutura_mision.Circle',
        null=True,
        blank=True,
        related_name='member'
    )
    is_lead = models.BooleanField(default=False)
    cart = models.ForeignKey('ciudadfutura_cart.Cart', null=True)


def set_username_and_email(sender, instance, **kwargs):

    # Means that was created via username
    if instance.username:
        instance.email = instance.username

    # Means that was created via email (no username)
    elif instance.email:
        instance.username = instance.email

    # Means that was created without username nor email
    elif not instance.email and not instance.username:
        instance.username = generate_unique_username()


# Attach signals
pre_save.connect(set_username_and_email, sender='ciudadfutura_auth.User')
