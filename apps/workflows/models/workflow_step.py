from apps.defaults.models.base_model import BaseModel
from apps.authentication.models.company import Company
from django.db import models

from apps.workflows.models.workflow import Workflow

class WorkflowStep(BaseModel):
    """
    - Workflow Steps are each action that is taken in a workflow.
    """

    workflow_step_name = models.CharField(max_length=40, help_text="Workflow Step Name", verbose_name="Name")
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Workflow Step'
        verbose_name_plural = 'Workflow Steps'

    def __str__(self):
        return self.workflow_step_name

    def save(self, *args, **kwargs):
        self.company = self.workflow.company
        super().save(*args, **kwargs)
    

    