from django.contrib import admin
from apps.authentication.models.company_profile_set import CompanyProfileSet
from apps.authentication.models.profile import Profile
from apps.defaults.admin import BaseModelAdmin
from apps.workflows.models.workflow_sequence import WorkflowSequence
from apps.workflows.models.workflow_step_action import WorkflowStepAction
from apps.workflows.models.workflow_step_approval import WorkflowStepApproval
from apps.workflows.models.workflow_step_form import WorkflowStepForm


class WorkflowSequenceAdmin(BaseModelAdmin):
    list_extend = ('workflow_name', 'step_name', 'type', 'order', 'company_name',)
    search_fields_extend = ('worflow__workflow_name', 'company_name',)
    readonly_fields = ('company', 'type',)
    list_filter = ('workflow__workflow_name',)
    
    def workflow_name(self, obj):
        return f"{obj.workflow.workflow_name}"
    
    def step_name(self, obj):
        step_name = ''
        if obj.type == 'Form':
            step_name = f"{obj.form_step.workflow_step_name}"
        elif obj.type == 'Approval':
            step_name = f"{obj.approval_step.workflow_step_name}"
        elif obj.type == 'Action':
            step_name = f"{obj.action_step.workflow_step_name}"
        
        return step_name

    def company_name(self, obj):
        return f"{obj.workflow.company.company_name}"

admin.site.register(WorkflowSequence, WorkflowSequenceAdmin)