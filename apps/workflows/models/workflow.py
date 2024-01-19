from apps.defaults.models.base_model import BaseModel
from apps.authentication.models.company import Company
from django.db import models

class Workflow(BaseModel):
    """
    - This model holds the workflows that are created by each company
    - Triggers a signal that adds the workflow to the admin Role of the company
    """

    workflow_name = models.CharField(max_length=40, help_text="Workflow Name", verbose_name="Name")
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Workflow'
        verbose_name_plural = 'Workflows'

    def __str__(self):
        return self.workflow_name
    