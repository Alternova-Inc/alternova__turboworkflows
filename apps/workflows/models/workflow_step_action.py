from django.db import models
from apps.workflows.models.workflow_step import WorkflowStep


class WorkflowStepAction(WorkflowStep):
    """
    - Actions that the system will execute
    - All actions point to abstract classes that are instantiated to perform the action itself
    - We dynamically instantiate the class by its name, on a specific path, and passing kwargs to it.
    - Some classes might reequite .env variables, and that is fine. The class itself should have it documented.
    """

    class_name = models.CharField(max_length=50)
    module_path = models.CharField(max_length=140, help_text="Example: apps.workflows.action_classes")
    class_kwargs = models.JSONField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Action Step'
        verbose_name_plural = 'Action Steps'
    
    def execute(self):
        """
        - This method will execute the action
        """
        import importlib
        module = importlib.import_module(self.module_path)
        class_pointer = getattr(module, self.class_name)
        mailgun_email = class_pointer(**self.class_kwargs)
        mailgun_email.send()
        del mailgun_email
