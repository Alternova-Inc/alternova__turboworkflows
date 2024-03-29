from apps.defaults.models.base_model import BaseModel
from apps.authentication.models.company import Company
from django.db import models

from apps.workflows.models.workflow import Workflow

class WorkflowStep(BaseModel):
    """
    - Workflow Steps are each action that is taken in a workflow.
    """

    workflow_step_name = models.CharField(max_length=40, help_text="Workflow Step Name", verbose_name="Name")
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Workflow Step'
        verbose_name_plural = 'Workflow Steps'
        abstract = True

    def __str__(self):
        return f'{self.workflow_step_name} - {self.company.company_name}'
    