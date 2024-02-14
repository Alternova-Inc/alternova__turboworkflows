from apps.defaults.models.base_model import BaseModel
from django.db import models
from apps.authentication.models.company import Company


class CompanyDepartment(BaseModel):
    """
    - This model represents the departments of a company.
    """

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=40, help_text="Department Name", verbose_name="Name")

    class Meta:
        verbose_name = 'Company Department'
        verbose_name_plural = 'Company Departments'

    def __str__(self):
        return f"{self.department_name} - {self.company.company_name}"
    