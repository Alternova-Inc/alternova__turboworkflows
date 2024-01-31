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
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'User Form Content'
        verbose_name_plural = 'User Form Contents'
        ordering = ['order']
        unique_together = ['user_form', 'order']

    def __str__(self):
        return f'{self.user_form.user_form_name} Content - {self.company.company_name}'

    def clean(self):
        if self.user_form.company != self.field.company:
            raise ValidationError("User Form must belong to the same company as the User Form Field.")

    def validate_company(self, *args, **kwargs):
        from apps.authentication.models.company_profile_set import CompanyProfileSet
        # validate that the user_form belongs to the same company as the user
        # In order for the validation to work we need to pass the user to the save method
        current_user = kwargs['current_user']
        if not current_user.is_superuser:
            profile_companies = CompanyProfileSet.objects.filter(profile__user=current_user)
            for company in profile_companies:
                if self.user_form.company.id == company.id:
                    raise ValidationError("User Form must belong to the same company as the user.")
        
    def save(self, *args, **kwargs):            
        self.full_clean()

        if hasattr(self, 'current_user'):
            self.validate_company(self, current_user=self.current_user)
            del self.current_user

        if hasattr(kwargs, 'current_user'):
            current_user = kwargs.pop('current_user', None)
            self.validate_company(self, current_user=current_user)

        # Always save the company automatically
        self.company = self.user_form.company
        super().save(*args, **kwargs)
        