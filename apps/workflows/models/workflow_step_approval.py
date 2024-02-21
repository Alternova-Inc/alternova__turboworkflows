from django.forms import ValidationError
from apps.authentication.models.company_position import CompanyPosition
from apps.workflows.models.workflow_step import WorkflowStep
from django.db import models


class WorkflowStepApproval(WorkflowStep):
    """
    - Approvals people will make
    """ 

    required_position = models.ForeignKey(CompanyPosition, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Approval Step'
        verbose_name_plural = 'Approval Steps'
        unique_together = ('company', 'required_position') # This is to ensure that there is only one approval step per company and position. This will avoid two steps that are the approval of the CEO

    def clean(self):
        if not self.required_position.is_approver:
            raise ValidationError("The required position must be an approver.")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
