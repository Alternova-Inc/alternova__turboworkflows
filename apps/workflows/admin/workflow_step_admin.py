from django.contrib import admin

from apps.defaults.admin import BaseModelAdmin
from apps.workflows.models.workflow_step_action import WorkflowStepAction
from apps.workflows.models.workflow_step_approval import WorkflowStepApproval
from apps.workflows.models.workflow_step_form import WorkflowStepForm


class WorkflowStepAdmin(BaseModelAdmin):

    list_extend = ('workflow_step_name', 'company_name',)
    search_fields_extend = ('workflow_step_name',)
    list_filter = ('company',)
    
    def company_name(self, obj):
        return f"{obj.company.company_name}"
    

class FormWorkflowStepAdmin(WorkflowStepAdmin):
    list_extend = ('workflow_step_name', 'company_name',)
    search_fields_extend = ('workflow_step_name', 'company_name',)
    list_filter = ('company',)
    
    def company_name(self, obj):
        return f"{obj.company.company_name}"


class ActionWorkflowStepAdmin(WorkflowStepAdmin):
    list_extend = ('workflow_step_name', 'company_name', 'class_name', 'module_path')
    search_fields_extend = ('workflow_step_name', 'company_name',)
    list_filter = ('company',)
    
    def company_name(self, obj):
        return f"{obj.company.company_name}"
    
    # Execute the action. Mostly to test the action
    def execute_action(modeladmin, request, queryset):
        for obj in queryset:
            obj.execute(test_run=True)

    execute_action.short_description = "Test selected actions execution"

    actions = [execute_action]


class ApprovalWorkflowStepAdmin(WorkflowStepAdmin):
    list_extend = ('workflow_step_name', 'company_name', 'required_position')
    search_fields_extend = ('workflow_step_name', 'company_name',)
    list_filter = ('company',)
    
    def company_name(self, obj):
        return f"{obj.company.company_name}"


admin.site.register(WorkflowStepForm, FormWorkflowStepAdmin)
admin.site.register(WorkflowStepAction, ActionWorkflowStepAdmin)
admin.site.register(WorkflowStepApproval, ApprovalWorkflowStepAdmin)