from apps.workflows.models.workflow_step import WorkflowStep


class WorkflowStepApproval(WorkflowStep):
    """
    - Approvals people will make
    """ 

    class Meta:
        verbose_name = 'Approval Step'
        verbose_name_plural = 'Approval Steps'