from django.contrib import admin
from apps.defaults.admin import BaseModelAdmin
from apps.workflows.models.workflow_step_action import WorkflowStepAction
from apps.workflows.models.workflow_step_approval import WorkflowStepApproval
from apps.workflows.models.workflow_step_form import WorkflowStepForm
from apps.workflows.models.workflow import Workflow

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
    pass


class ActionWorkflowStepAdmin(WorkflowStepAdmin):
    pass

class ApprovalWorkflowStepAdmin(WorkflowStepAdmin):
    pass


admin.site.register(Workflow, WorkflowAdmin)
admin.site.register(WorkflowStepForm, FormWorkflowStepAdmin)
admin.site.register(WorkflowStepAction, ActionWorkflowStepAdmin)
admin.site.register(WorkflowStepApproval, ApprovalWorkflowStepAdmin)
