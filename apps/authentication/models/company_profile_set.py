from django.forms import ValidationError
from apps.authentication.models.company_department import CompanyDepartment
from apps.authentication.models.company_position import CompanyPosition
from apps.authentication.models.role import Role
from apps.defaults.models.base_model import BaseModel
from django.db import models
from apps.authentication.models.company import Company
from apps.authentication.models.profile import Profile

class CompanyProfileSet(BaseModel):
    """
    - This model represents the relationship between a company and a profile.
    - The role is the one that defines the permissions that the profile has in the company.
    """

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(CompanyDepartment, on_delete=models.SET_NULL, null=True)
    position = models.ForeignKey(CompanyPosition, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Company-Profile Set'
        verbose_name_plural = 'Company-Profile Sets'

    def clean(self):
        if self.company != self.role.company:
            raise ValidationError("Selected company and role's company must be the same.")
        
        if self.company != self.department.company:
            raise ValidationError("Selected company and department's company must be the same.")
        
        if self.company != self.position.company:
            raise ValidationError("Selected company and position's company must be the same.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
        