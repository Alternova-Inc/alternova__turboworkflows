from apps.defaults.models.status_message import StatusMessage

def main_admin_context(request):
    """
    Returns a dictionary containing the status messages for the main admin context.
    """
    status_messages = list(StatusMessage.objects.filter(is_active=True))
    return {'status_messages': status_messages}
