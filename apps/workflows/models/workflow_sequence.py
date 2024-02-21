from django.forms import ValidationError
from apps.authentication.models.company import Company
from apps.defaults.models.base_model import BaseModel
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from apps.workflows.models import Workflow, WorkflowStepForm, WorkflowStepAction, WorkflowStepApproval


class WorkflowSequence(BaseModel):
    '''
    - This model represents the relationship between a workflow and several steps.
    - Steps are given an order to be displayed in the user form.
    '''

    TYPE_CHOICES = [
        ('Form', 'Form'),
        ('Approval', 'Approval'),
        ('Action', 'Action'),
    ]

    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE)
    form_step = models.ForeignKey(WorkflowStepForm, on_delete=models.CASCADE, blank=True, null=True)
    approval_step = models.ForeignKey(WorkflowStepApproval, on_delete=models.CASCADE, blank=True, null=True)
    action_step = models.ForeignKey(WorkflowStepAction, on_delete=models.CASCADE, blank=True, null=True)
    order = models.PositiveIntegerField()
    type = models.CharField(max_length=255, choices=TYPE_CHOICES, blank=True, null=True)

    class Meta:
        verbose_name = 'Workflow Sequence'
        verbose_name_plural = 'Workflow Sequences'
        ordering = ['order']
        unique_together = ['workflow', 'order']

    def __str__(self):
        return f'{self.workflow.workflow_name} - Sequence'

    def clean(self):
        if not self.form_step and not self.approval_step and not self.action_step:
            raise ValidationError("At least one of form_step, approval_step, or action_step must be selected.")

        if self.form_step and (self.approval_step or self.action_step):
            raise ValidationError("Only one of form_step, approval_step, or action_step can be filled.")

        elif self.approval_step and (self.form_step or self.action_step):
            raise ValidationError("Only one of form_step, approval_step, or action_step can be filled.")

        elif self.action_step and (self.form_step or self.approval_step):
            raise ValidationError("Only one of form_step, approval_step, or action_step can be filled.")

    def validate_company(self, *args, **kwargs):
        from apps.authentication.models.company_profile_set import CompanyProfileSet
        
        current_user = kwargs['current_user']
        type = kwargs['type']

        # first, validate that worflow and the selected step belong to the same company
        if type == 'Form':
            if self.workflow.company != self.form_step.company:
                raise ValidationError("Workflow and Form Step must belong to the same company.")
        elif type == 'Approval':
            if self.workflow.company != self.approval_step.company:
                raise ValidationError("Workflow and Approval Step must belong to the same company.")
        elif type == 'Action':
            if self.workflow.company != self.action_step.company:
                raise ValidationError("Workflow and Action Step must belong to the same company.")

    def save(self, *args, **kwargs):            
        self.full_clean()
        
        # Always save the type automatically
        if self.form_step:
            self.type = 'Form'
        elif self.approval_step:
            self.type = 'Approval'
        elif self.action_step:
            self.type = 'Action'

        super().save(*args, **kwargs)
        