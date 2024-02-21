from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.authentication.models.role import Role
from apps.authentication.models.company import Company

@receiver(post_save, sender=Company)
def create_role_for_company(sender, instance, created, **kwargs):
    """
    - Create default roles for a company when it is created.
    """
    if created:
        Role.objects.create(company=instance, role_name='default', is_default=True)
        Role.objects.create(company=instance, role_name='admin')
        