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
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.CharField(max_length=255)
    step = GenericForeignKey('content_type', 'object_id')
    order = models.PositiveIntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    type = models.CharField(max_length=255, choices=TYPE_CHOICES, blank=True, null=True)

    class Meta:
        verbose_name = 'Workflow Sequence'
        verbose_name_plural = 'Workflow Sequences'
        ordering = ['order']
        unique_together = ['workflow', 'order']

    def __str__(self):
        return f'{self.worfklow.workflow_name} - Sequence'

    def clean(self):
        if isinstance(self.step, (WorkflowStepForm, WorkflowStepAction, WorkflowStepApproval)):
            self.type = self.step.__class__.__name__
        else:
            raise ValidationError("Invalid step type.")
        
    #     if self.workflow.company != self.step.company:
    #         raise ValidationError("User Form must belong to the same company as the User Form Field.")

    # def validate_company(self, *args, **kwargs):
    #     from apps.authentication.models.company_profile_set import CompanyProfileSet
    #     # validate that the user_form belongs to the same company as the user
    #     # In order for the validation to work we need to pass the user to the save method
    #     current_user = kwargs['current_user']
    #     if not current_user.is_superuser:
    #         profile_companies = CompanyProfileSet.objects.filter(profile__user=current_user)
    #         for company in profile_companies:
    #             if self.user_form.company.id == company.id:
    #                 raise ValidationError("User Form must belong to the same company as the user.")
        
    def save(self, *args, **kwargs):            
        self.full_clean()

        # if hasattr(self, 'current_user'):
        #     self.validate_company(self, current_user=self.current_user)
        #     del self.current_user

        # if hasattr(kwargs, 'current_user'):
        #     current_user = kwargs.pop('current_user', None)
        #     self.validate_company(self, current_user=current_user)

        # # Always save the company automatically
        # self.company = self.user_form.company

        super().save(*args, **kwargs)