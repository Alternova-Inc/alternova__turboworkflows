from apps.workflows.models.workflow_step import WorkflowStep


class WorkflowStepForm(WorkflowStep):
    """
    - Forms that people will fill
    """

    class Meta:
        verbose_name = 'Form Step'
        verbose_name_plural = 'Form Steps'