from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new User"""
        if not email:
            raise ValueError('Users must have an email address!')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)  # self._db - for different DBs ?

        return user


#  PermissionsMixin class is used to work with permissions using our User
class User(AbstractBaseUser, PermissionsMixin):
    # don't forget to make email unique as far
    # we gonna use it as username
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    # This field is a predefined field of AbstractBaseUser
    USERNAME_FIELD = 'email'
