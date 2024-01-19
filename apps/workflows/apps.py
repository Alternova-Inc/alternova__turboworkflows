from django.apps import AppConfig


class WorkflowsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.workflows'

    def ready(self):
        # Import the signals module so that it gets loaded when the application starts
        import apps.workflows.signals
