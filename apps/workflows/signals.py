from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.authentication.models.role import Role
from apps.workflows.models.workflow import Workflow

@receiver(post_save, sender=Workflow)
def create_role_for_company(sender, instance, created, **kwargs):
    if created:
        # Get the admin role for the company
        admin_role = Role.objects.get(company=instance.company, role_name='admin')
        # Add the new workflow to the admin role's workflows
        admin_role.workflows.add(instance)
        