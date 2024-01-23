from apps.defaults.models.base_model import BaseModel
from apps.authentication.models.company import Company
from django.db import models
from apps.defaults.models.base_polymorphic_model import BasePolymorphicModel

from apps.workflows.models.workflow import Workflow

class WorkflowStep(BasePolymorphicModel):
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
    

class FormWorkflowStep(WorkflowStep):
    """
    - Forms that people will fill
    """

    class Meta:
        verbose_name = 'Form Step'
        verbose_name_plural = 'Form Steps'


class ActionWorkflowStep(WorkflowStep):
    """
    - Actions that the system will execute
    """ 
    
    class Meta:
        verbose_name = 'Action Step'
        verbose_name_plural = 'Action Steps'


class ApprovalWorkflowStep(WorkflowStep):
    """
    - Approvals people will make
    """ 

    class Meta:
        verbose_name = 'Approval Step'
        verbose_name_plural = 'Approval Steps'
    