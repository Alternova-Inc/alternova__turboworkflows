from apps.workflows.models.workflow_step import WorkflowStep


class WorkflowStepForm(WorkflowStep):
    """
    - Forms that people will fill
    - Forms shown to users for users to fill in order to request something.
    """

    class Meta:
        verbose_name = 'Form Step'
        verbose_name_plural = 'Form Steps'