from django.forms import ValidationError
from apps.authentication.models.company import Company
from apps.defaults.models.base_model import BaseModel
from django.db import models
from apps.workflows.models.user_form_field import UserFormField
from apps.workflows.models.workflow_step_form import WorkflowStepForm


class UserFormContent(BaseModel):
    '''
    - This model represents the relationship between a user form and several form fields.
    - Form fields are given an order to be displayed in the user form.
    '''
    user_form = models.ForeignKey(WorkflowStepForm, on_delete=models.CASCADE)
    field = models.ForeignKey(UserFormField, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    is_required = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'User Form Content'
        verbose_name_plural = 'User Form Contents'
        ordering = ['order']
        unique_together = ['user_form', 'order']

    def __str__(self):
        return f'{self.user_form.workflow_step_name} Content - {self.user_form.company.company_name}'

    def clean(self):
        if self.user_form.company != self.field.company:
            raise ValidationError("User Form must belong to the same company as the User Form Field.")                    
        
    def save(self, *args, **kwargs):            
        self.full_clean()
        super().save(*args, **kwargs)
        