from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not phone:
            raise ValueError("Users must have an email address")

        user = self.model(
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            phone,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="آدرس ایمیل",
        max_length=255,
        unique=True,
        null=True,
        blank=True,
    )
    fullname = models.CharField(
        max_length=50,
        verbose_name='نام کامل'
    )
    phone = models.CharField(
        max_length=12,
        unique=True,
        verbose_name="شماره تلفن"
    )
    image = models.ImageField(
        blank=True,
        null=True,
        verbose_name="عکس پروفایل کاربر",
        upload_to='profile_pics'
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False, verbose_name='ادمین')

    objects = UserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = 'کاربرها'

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Otp(models.Model):
    token = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=11)
    code = models.IntegerField()
    exppiration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone
