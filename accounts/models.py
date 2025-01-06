from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

User = settings.AUTH_USER_MODEL


class UserModelManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        if not username:
            raise ValueError("Users must have an username address")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, password=None):
        # if len(password) < 8:
        #     raise ValueError("Password must be bigger than 8 Char")

        user = self.create_user(
            email,
            username,
            first_name,
            last_name,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserModel(AbstractBaseUser, PermissionsMixin):
    class GENDER(models.TextChoices):
        MALE = "Male", "Male"
        FEMALE = "Female", "Female"

    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=225, unique=True)
    # All Users
    first_name = models.CharField(max_length=225)
    middle_name = models.CharField(max_length=225, blank=True, null=True)
    last_name = models.CharField(max_length=225)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(
        max_length=10, choices=GENDER.choices, blank=True, null=True
    )
    phone_number = models.CharField(max_length=225, null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)
    # permissions
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_nurse = models.BooleanField(default=False)

    objects = UserModelManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    def __str__(self):
        return self.email

    def full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}".title()

    def get_employeed_id(self):
        if self.is_nurse:
            return self.id + 182343
        return None


class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ssn = models.IntegerField(blank=True, null=True)
    race = models.CharField(max_length=225, blank=True, null=True)
    occupation = models.CharField(max_length=225, blank=True, null=True)
    medical_history = models.TextField(max_length=1500, blank=True, null=True)

    def __str__(self):
        return str(self.user)

    @receiver(post_save, sender=User)
    def create_patient_profile(sender, instance, created, **kwargs):
        patient = instance.is_admin or instance.is_nurse
        if not patient and created:
            PatientProfile.objects.create(user=instance)
