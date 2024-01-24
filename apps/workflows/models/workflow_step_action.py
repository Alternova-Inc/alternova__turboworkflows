from apps.workflows.models.workflow_step import WorkflowStep


class WorkflowStepAction(WorkflowStep):
    """
    - Actions that the system will execute
    """ 
    
    class Meta:
        verbose_name = 'Action Step'
        verbose_name_plural = 'Action Steps'