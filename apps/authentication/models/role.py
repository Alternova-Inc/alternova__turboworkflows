from apps.defaults.models.base_model import BaseModel
from apps.workflows.models.workflow import Workflow
from apps.authentication.models.company import Company
from django.db import models
from django.core.exceptions import ValidationError


class Role(BaseModel):
    """
    - This model holds the permissions that a group of users can have
    - When creating an organization two roles are created by default: default and admin
    - The default role is assigned to all users that are created in the organization. This role will not be populated by default.
    - The admin model will be assigned to the user that creates the organization. This role will be populated by default with every new workflow that is created
    """

    role_name = models.CharField(max_length=40, help_text="Role Name", verbose_name="Name")
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    workflows = models.ManyToManyField(Workflow, blank=True)
    is_default = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return f'{self.role_name} - {self.company.company_name}'
    
    def clean(self):
        if self.is_default and Role.objects.filter(company=self.company, is_default=True).exclude(pk=self.pk).exists():
            raise ValidationError("A default role for this company already exists.")
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
