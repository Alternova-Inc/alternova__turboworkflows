from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.authentication.models.role import Role
from apps.workflows.models.workflow import Workflow

@receiver(post_save, sender=Workflow)
def add_workflow_to_role(sender, instance, created, **kwargs):
    """
    Add a workflow to the admin role's workflows if the instance is newly created.
    """
    if created:
        # Get the admin role for the company
        admin_role = Role.objects.get(company=instance.company, role_name='admin')
        # Add the new workflow to the admin role's workflows
        admin_role.workflows.add(instance)
        