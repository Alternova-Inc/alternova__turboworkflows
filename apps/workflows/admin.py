from django.contrib import admin
from apps.defaults.admin import BaseModelAdmin, BasePolymorphicParentModelAdmin
from polymorphic.admin import PolymorphicChildModelAdmin
from apps.workflows.models.workflow import Workflow
from apps.workflows.models.workflow_step import WorkflowStep, FormWorkflowStep, ActionWorkflowStep, ApprovalWorkflowStep

# Register your models here.
class WorkflowAdmin(BaseModelAdmin):
    list_extend = ('workflow_name', 'company_name',)
    search_fields_extend = ('workflow_name', 'company__company_name',)

    def company_name(self, obj):
        return f"{obj.company.company_name}"
    

class FormWorkflowStepAdmin(PolymorphicChildModelAdmin):
    base_model = FormWorkflowStep

    # By using these `base_...` attributes instead of the regular ModelAdmin `form` and `fieldsets`,
    # the additional fields of the child models are automatically added to the admin form.
    # base_form = ...
    # base_fieldsets = (
    #     type,
    # )


class ActionWorkflowStepAdmin(PolymorphicChildModelAdmin):
    base_model = ActionWorkflowStep

    # By using these `base_...` attributes instead of the regular ModelAdmin `form` and `fieldsets`,
    # the additional fields of the child models are automatically added to the admin form.
    # base_form = ...
    # base_fieldsets = (
    #     type,
    # )

class ApprovalWorkflowStepAdmin(PolymorphicChildModelAdmin):
    base_model = ApprovalWorkflowStep

    # By using these `base_...` attributes instead of the regular ModelAdmin `form` and `fieldsets`,
    # the additional fields of the child models are automatically added to the admin form.
    # base_form = ...
    # base_fieldsets = (
    #     type,
    # )

class WorkflowStepAdmin(BasePolymorphicParentModelAdmin):
    base_model = WorkflowStep 
    child_models = (FormWorkflowStep, ActionWorkflowStep, ApprovalWorkflowStep,)

    list_extend = ('workflow_step_name', 'workflow_name', 'company_name', 'get_type',)
    search_fields_extend = ('workflow_step_name', 'workflow__workflow_name', 'company__company_name',)
    readonly_fields = ('company',)

    def workflow_name(self, obj):
        return f"{obj.workflow.workflow_name}"
    
    def company_name(self, obj):
        return f"{obj.company.company_name}"
    
    def get_type(self, obj):
        return obj.get_real_instance_class()._meta.verbose_name
    get_type.short_description = 'Type'


admin.site.register(Workflow, WorkflowAdmin)
admin.site.register(FormWorkflowStep, FormWorkflowStepAdmin)
admin.site.register(ActionWorkflowStep, ActionWorkflowStepAdmin)
admin.site.register(ApprovalWorkflowStep, ApprovalWorkflowStepAdmin)
admin.site.register(WorkflowStep, WorkflowStepAdmin)
