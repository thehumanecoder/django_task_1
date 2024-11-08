from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.JSONField(blank=True, null=True)
    profile_handle = models.CharField(
        max_length=30,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9_]+$',
                message="Profile handle must be alphanumeric or contain underscores only."
            )
        ]
    )
    
    def __str__(self):
        return f"{self.user.username}'s profile"