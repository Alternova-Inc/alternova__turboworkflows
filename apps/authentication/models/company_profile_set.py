from apps.authentication.models.role import Role
from apps.defaults.models.base_model import BaseModel
from django.db import models
from apps.authentication.models.company import Company
from apps.authentication.models.profile import Profile

class CompanyProfileSet(BaseModel):
    """
    - This model represents any user in the platform.
    - Extends the Django's default user model.
    """

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Company-Profile Set'
        verbose_name_plural = 'Company-Profile Sets'
