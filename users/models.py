from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.mail import send_mail
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None):
        if not email:
            raise ValueError('Users must have an email address!')

        user = self.model(
            email=self.normalize_email(email)
        )
        user.full_name = full_name
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password=None):
        user = self.create_user(
            email=email,
            full_name=full_name,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    image = models.ImageField(
        upload_to='users/%Y/%m', 
        null=True, 
        blank=True
    )
    email = models.EmailField(unique=True)
    full_name = models.CharField(
        max_length=15,
        null=True, 
        blank=True
    )

    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    creation_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-creation_time',]

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    def send_otp(self):
        return send_mail(
            "Confirmation OTP",
            f"Your account confirmation OTP code is: {self.otp_code}",
            "support@incident_report.com",
            [self.email],
            fail_silently=True
        )
    
    def send_password_change_email(self, password):
        return send_mail(
            "Password Change Alert",
            f"Your password has been chamged to {password}, make sure to change it to a secure one.",
            "support@incident_report.com",
            [self.email],
            fail_silently=True
        )
    
    def update_user_password(self, password):
        self.set_password(password)
        return self.save()
    
