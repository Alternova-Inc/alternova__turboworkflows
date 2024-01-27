from django.contrib import admin
from apps.authentication.models.company_profile_set import CompanyProfileSet
from apps.authentication.models.profile import Profile
from apps.defaults.admin import BaseModelAdmin
from apps.workflows.models.user_form_field import UserFormField
from apps.workflows.models.user_form_content import UserFormContent
from apps.workflows.models.workflow_step_action import WorkflowStepAction
from apps.workflows.models.workflow_step_approval import WorkflowStepApproval
from apps.workflows.models.workflow_step_form import WorkflowStepForm
from apps.workflows.models.workflow import Workflow
from django.shortcuts import redirect
from django.urls import reverse

# Register your models here.
class WorkflowAdmin(BaseModelAdmin):
    list_extend = ('workflow_name', 'company_name',)
    search_fields_extend = ('workflow_name', 'company__company_name',)

    def company_name(self, obj):
        return f"{obj.company.company_name}"
    
class WorkflowStepAdmin(BaseModelAdmin):

    list_extend = ('workflow_step_name', 'workflow_name', 'company_name',)
    search_fields_extend = ('workflow_step_name', 'workflow__workflow_name',)
    readonly_fields = ('company',)
    list_filter = ('company',)

    def workflow_name(self, obj):
        return f"{obj.workflow.workflow_name}"
    
    def company_name(self, obj):
        return f"{obj.company.company_name}"
    

class FormWorkflowStepAdmin(WorkflowStepAdmin):
    list_extend = ('workflow_step_name', 'company_name',)
    search_fields_extend = ('workflow_step_name', 'company_name',)
    list_filter = ('company',)
    
    def company_name(self, obj):
        return f"{obj.company.company_name}"


class ActionWorkflowStepAdmin(WorkflowStepAdmin):
    pass


class ApprovalWorkflowStepAdmin(WorkflowStepAdmin):
    pass

    
class UserFormFieldAdmin(BaseModelAdmin):
    list_extend = ('code', 'public_name', 'type', 'company_name',)
    search_fields_extend = ('public_name', 'company__company_name',)
    list_filter = ('company',)
    
    def company_name(self, obj):
        return f"{obj.company.company_name}"
    

class UserFormContentAdmin(BaseModelAdmin):
    list_extend = ('user_form_name', 'form_field_name', 'order', 'company_name',)
    search_fields_extend = ('user_form__workflow_step_name', 'field__public_name', 'company_name',)
    readonly_fields = ('company',)
    
    def user_form_name(self, obj):
        return f"{obj.user_form.workflow_step_name}"
    
    def form_field_name(self, obj):
        return f"{obj.field.public_name}"

    def company_name(self, obj):
        return f"{obj.company.company_name}"
    
    # code to filter selects by company
    def get_form(self, request, obj=None, **kwargs):
        Form = super().get_form(request, obj, **kwargs)

        # Define a new form class that accepts a 'request' argument
        class RequestForm(Form):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

                user = request.user
                if user and not user.is_superuser:
                    # get the profile of the user
                    profile = Profile.objects.get(user=user)

                    # get the companies of the user
                    user_companies = CompanyProfileSet.objects.filter(profile=profile).values_list('company', flat=True)

                    # get the available fields for the user
                    self.fields['fields'].queryset = UserFormField.objects.filter(company__in=user_companies)
                    self.fields['user_form'].queryset = WorkflowStepForm.objects.filter(company__in=user_companies)

        # Return the new form class
        return RequestForm
    
    # pass the current user from the django admin to the save() method.
    def save_model(self, request, obj, form, change):
        obj.current_user = request.user
        super().save_model(request, obj, form, change)
    

admin.site.register(Workflow, WorkflowAdmin)
admin.site.register(WorkflowStepForm, FormWorkflowStepAdmin)
admin.site.register(WorkflowStepAction, ActionWorkflowStepAdmin)
admin.site.register(WorkflowStepApproval, ApprovalWorkflowStepAdmin)
admin.site.register(UserFormField, UserFormFieldAdmin)
admin.site.register(UserFormContent, UserFormContentAdmin)
