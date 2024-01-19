from django.contrib import admin
from apps.defaults.admin import BaseModelAdmin

from apps.workflows.models.workflow import Workflow

# Register your models here.
class WorkflowAdmin(BaseModelAdmin):
    list_extend = ('workflow_name',)
    search_fields_extend = ('workflow_name',)


admin.site.register(Workflow, WorkflowAdmin)
