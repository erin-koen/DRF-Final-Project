from django.contrib.auth.models import AbstractUser, BaseUserManager


# look this up - manages creation/deletion/edit of user model
class UserManager(BaseUserManager):
    pass


# this is what ^ is managing
class CustomUser(AbstractUser):
    objects = UserManager()
