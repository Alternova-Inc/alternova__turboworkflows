from apps.defaults.models.base_model import BaseModel
from apps.workflows.models.workflow import Workflow
from apps.authentication.models.company import Company
from django.db import models


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

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.role_name
    