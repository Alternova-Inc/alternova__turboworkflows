from django.contrib import admin

from apps.workflows.models.workflow import Workflow

# Register your models here.
class WorkflowAdmin(admin.ModelAdmin):
    list_display = ('id', 'workflow_name')


admin.site.register(Workflow, WorkflowAdmin)
