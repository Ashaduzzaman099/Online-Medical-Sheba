# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, full_name, user_name, phone_number, date_of_birth, password=None, **extra_fields):
      """
      Creates and saves a User with the given email, full_name, user_name, 
      phone_number, date_of_birth, and password.
      """
      if not email:
         raise ValueError("Users must have an email address")
      if not full_name:
         raise ValueError("Users must have a full name")
      if not user_name:
         raise ValueError("Users must have a username")
      if not phone_number:
         raise ValueError("Users must have a phone number")
      if not date_of_birth:
         raise ValueError("Users must have a date of birth")

      email = self.normalize_email(email)
      user = self.model(
         email=email,
         full_name=full_name,
         user_name=user_name,
         phone_number=phone_number,
         date_of_birth=date_of_birth,
         **extra_fields  # Dynamically handle additional fields like 'role'
      )

      if password:
         user.set_password(password)
      user.save(using=self._db)
      return user


    def create_superuser(self, email, full_name, user_name, phone_number, date_of_birth, password=None, **extra_fields):
      """
      Creates and saves a superuser with the given email, full_name, user_name, 
      phone_number, date_of_birth, and password.
      """
      extra_fields.setdefault('role', 'admin')  # Ensure role is set to 'admin'
      extra_fields.setdefault('is_admin', True)
      extra_fields.setdefault('is_staff', True)
      extra_fields.setdefault('is_superuser', True)

      if extra_fields.get('role') != 'admin':
         raise ValueError("Superusers must have role='admin'")
      if not extra_fields.get('is_admin'):
         raise ValueError("Superusers must have is_admin=True")
      if not extra_fields.get('is_staff'):
         raise ValueError("Superusers must have is_staff=True")
      if not extra_fields.get('is_superuser'):
         raise ValueError("Superusers must have is_superuser=True")

      return self.create_user(
         email,
         full_name,
         user_name,
         phone_number,
         date_of_birth,
         password,
         **extra_fields
      )


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True,
    )
    full_name = models.CharField(max_length=255)
    user_name = models.CharField(
        verbose_name="Username",
        max_length=100,
        unique=True,
    )
    phone_number = models.CharField(
        verbose_name="Phone Number",
        max_length=11,
        unique=True,
    )
    date_of_birth = models.DateField()

    # Role field with predefined choices
    ROLE_CHOICES = [
        ('user', 'User/Patient'),
        ('doctor', 'Doctor'),
        ('admin', 'Admin'),  # Include admin role explicitly
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    # Blood group and donation fields
    blood_group = models.CharField(
        max_length=3,
        choices=[
            ("A+", "A+"), ("A-", "A-"),
            ("B+", "B+"), ("B-", "B-"),
            ("AB+", "AB+"), ("AB-", "AB-"),
            ("O+", "O+"), ("O-", "O-")
        ],
        null=True,
        blank=True,
    )

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
        null=True,
        blank=True,
    )
    wants_to_donate_blood = models.BooleanField(default=False)

    profile_pic = models.ImageField(upload_to='profile_pic/', null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_doctor = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)  # Add this field
    is_superuser = models.BooleanField(default=False)  # Add this field

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['full_name', 'user_name', 'phone_number', 'date_of_birth', 'role']

    objects = UserManager()

    def __str__(self):
        return self.email
