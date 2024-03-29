from apps.defaults.models.base_model import BaseModel
from django.db import models

class Company(BaseModel):
    """
    - This model represents any company in the platform.
    - When a company is created a signal generates 2 roles: default and admin.
    """

    company_name = models.CharField(max_length=40, help_text="Company Name", verbose_name="Name")

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return f"{self.company_name}"
    