from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from users.helpers import RandomFileName
from users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField('email address', unique=True)
    is_staff = models.BooleanField('staff status', default=False,
        help_text='Designates whether the user can log into this admin site.')
    is_active = models.BooleanField('active', default=False,
        help_text='Designates whether this user should be treated as active. '
                  'Unselect this instead of deleting accounts.')
    avatar = models.ImageField(upload_to=RandomFileName('user_avatars/'),
                               null=True, blank=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
