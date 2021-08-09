from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


# Create your models here.
#
class UserManager(BaseUserManager):
    def create_user(self, email, username, password, alias=None):
        if not email:
            raise
        ValueError("Please Enter An Email Address")
        if not username:
            raise
        ValueError('Please Enter a Valid Username')
        if not password:
            raise
        ValueError('Please Enter a Password')
        if not alias:
            alias = username
        user = self.model(email=self.normalize_email(email),
                          username=username,
                          alias=alias)
        user.set_password(password)
        user.save()
        return user


def create_superuser(self, email, username, password, alias=None):
    self.create_user(email, username, password, alias)
    user.is_staff()
    user.is_superuser = True
    user.save()
    return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('user name'), max_length=30, unique=True)
    alias = models.CharField(_('alias'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'alias']

    def __str__(self):
        return
    "@{}".format(self.username)

    def get_short_name(self):
        return self.alias

    def get_long_name(self):
        return "{} @{}".format(self.alias, self.username)

