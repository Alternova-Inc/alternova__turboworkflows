from django.contrib import admin
from apps.defaults.admin import BaseModelAdmin

from apps.workflows.models.workflow import Workflow
from apps.workflows.models.workflow_step import WorkflowStep

# Register your models here.
class WorkflowAdmin(BaseModelAdmin):
    list_extend = ('workflow_name', 'company_name',)
    search_fields_extend = ('workflow_name', 'company__company_name',)

    def company_name(self, obj):
        return f"{obj.company.company_name}"

# Register your models here.
class WorkflowStepAdmin(BaseModelAdmin):
    list_extend = ('workflow_step_name', 'workflow_name', 'company_name',)
    search_fields_extend = ('workflow_step_name', 'workflow__workflow_name', 'company__company_name',)
    readonly_fields = ('company',)

    def workflow_name(self, obj):
        return f"{obj.workflow.workflow_name}"
    
    def company_name(self, obj):
        return f"{obj.company.company_name}"


admin.site.register(Workflow, WorkflowAdmin)
admin.site.register(WorkflowStep, WorkflowStepAdmin)
