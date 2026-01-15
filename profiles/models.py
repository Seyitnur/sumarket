from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

def generate_username():
    return f'user_{uuid.uuid4().hex[:8]}'

class User(AbstractUser):
    phone = models.CharField(max_length=12, unique=True)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set_permissions',
        blank=True,
        help_text='Specific permissions for this user.'
    )

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = generate_username()
        super().save(*args, **kwargs)
