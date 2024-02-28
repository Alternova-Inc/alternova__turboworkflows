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
    class_method = models.CharField(max_length=50, blank=True, null=True, help_text="If blank, code should run in constructor")
    class_kwargs = models.JSONField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Action Step'
        verbose_name_plural = 'Action Steps'
    
    def execute(self, test_run=False):
        """
        - This method will execute the action
        """
        import importlib
        module = importlib.import_module(self.module_path)
        class_pointer = getattr(module, self.class_name)

        # instantiates the class and passes the kwargs to it.
        # This executes the __init__ method
        self.class_kwargs['test_run'] = test_run
        class_instance = class_pointer(**self.class_kwargs) 

        if self.class_method:
            method = getattr(class_instance, self.class_method) # gets the method from the class
            method() # executes the method
        
        del class_instance # deletes the instance to free memory
