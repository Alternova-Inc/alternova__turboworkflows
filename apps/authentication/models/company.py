from apps.defaults.models.base_model import BaseModel
from django.db import models

class Company(BaseModel):
    """
    - This model represents any user in the platform.
    - Extends the Django's default user model.
    """

    company_name = models.CharField(max_length=40, help_text="Company Name", verbose_name="Name")

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return f"{self.company_name}"
    