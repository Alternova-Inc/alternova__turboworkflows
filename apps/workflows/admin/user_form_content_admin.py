from django.contrib import admin
from apps.authentication.models.company_profile_set import CompanyProfileSet
from apps.authentication.models.profile import Profile
from apps.defaults.admin import BaseModelAdmin
from apps.workflows.models.user_form_content import UserFormContent
from apps.workflows.models.user_form_field import UserFormField
from apps.workflows.models.workflow_step_form import WorkflowStepForm


class UserFormContentAdmin(BaseModelAdmin):
    list_extend = ('user_form_name', 'form_field_name', 'order', 'company_name',)
    search_fields_extend = ('user_form__workflow_step_name', 'field__public_name', 'company_name',)
    list_filter = ('user_form__workflow_step_name',)
    
    def user_form_name(self, obj):
        return f"{obj.user_form.workflow_step_name}"
    
    def form_field_name(self, obj):
        return f"{obj.field.public_name}"

    def company_name(self, obj):
        return f"{obj.user_form.company.company_name}"
    
admin.site.register(UserFormContent, UserFormContentAdmin)
