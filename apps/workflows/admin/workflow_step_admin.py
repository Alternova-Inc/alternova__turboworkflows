from django.contrib import admin

from apps.defaults.admin import BaseModelAdmin
from apps.workflows.models.workflow_step_action import WorkflowStepAction
from apps.workflows.models.workflow_step_approval import WorkflowStepApproval
from apps.workflows.models.workflow_step_form import WorkflowStepForm


class WorkflowStepAdmin(BaseModelAdmin):

    list_extend = ('workflow_step_name', 'company_name',)
    search_fields_extend = ('workflow_step_name',)
    readonly_fields = ('company',)
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
    pass


class ApprovalWorkflowStepAdmin(WorkflowStepAdmin):
    pass


admin.site.register(WorkflowStepForm, FormWorkflowStepAdmin)
admin.site.register(WorkflowStepAction, ActionWorkflowStepAdmin)
admin.site.register(WorkflowStepApproval, ApprovalWorkflowStepAdmin)