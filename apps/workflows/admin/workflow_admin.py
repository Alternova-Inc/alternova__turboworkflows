from django.contrib import admin
from apps.defaults.admin import BaseModelAdmin
from apps.workflows.models.workflow import Workflow


class WorkflowAdmin(BaseModelAdmin):
    list_extend = ('workflow_name', 'company_name',)
    search_fields_extend = ('workflow_name', 'company__company_name',)

    def company_name(self, obj):
        return f"{obj.company.company_name}"
    

admin.site.register(Workflow, WorkflowAdmin)
