from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from timezone_field import TimeZoneField


class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff,
                      is_superuser, **extra_fields):
        """
        Create and Save an User with email and password
            :param str email: user email
            :param str password: user password
            :param bool is_superuser: whether user admin or not
            :return users.models.User user: user
            :raise ValueError: email is not set
        """
        now = timezone.now()

        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        # is_active = extra_fields.pop("is_active", False)

        user = self.model(email=email, is_staff=is_staff,
                          is_superuser=is_superuser, last_login=now,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save an User with the given email and password.
        :param str email: user email
        :param str password: user password
        :return users.models.User user: admin user
        """
        is_staff = extra_fields.pop("is_staff", False)
        return self._create_user(email, password, True,True,
                                 **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        db_index=True
    )
    user_id = models.CharField(_("User Id"), max_length=20)
    real_name = models.CharField(_("Full name"), max_length=120)
    timezone_info = TimeZoneField(default='Asia/Kolkata')
    is_staff = models.BooleanField(
        _('staff status'), default=False, help_text=_(
            'Designates whether the user can log into this admin site.'))

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def get_short_name(self):
        # The user is identified by their email address
        return self.email


class ActivityPeriod(models.Model):
    """
    model to store user activity
    """
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    start_time = models.DateTimeField(_('Start Time'))
    end_time = models.DateTimeField(_('End Time'))
