from django.contrib.auth.models import User
from apps.defaults.models.base_model import BaseModel
from django.db import models

class Profile(BaseModel):
    """
    - This model represents any user in the platform.
    - Extends the Django's default user model.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
