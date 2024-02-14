from apps.defaults.models.base_model import BaseModel
from django.db import models
from apps.authentication.models.company import Company


class CompanyPosition(BaseModel):
    """
    - This model represents the positions available in a company.
    """

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position_name = models.CharField(max_length=40, help_text="Position Name", verbose_name="Name")
    is_approver = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Company Position'
        verbose_name_plural = 'Company Positions'

    def __str__(self):
        return f"{self.position_name} - {self.company.company_name}"