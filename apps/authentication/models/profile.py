from django.contrib.auth.models import User
from apps.authentication.models.role import Role
from apps.defaults.models.base_model import BaseModel
from django.db import models

class Profile(BaseModel):
    """
    - This model represents any user in the platform.
    - Extends the Django's default user model.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
