from apps.defaults.models.status_message import StatusMessage

def main_admin_context(request):
    status_messages = list(StatusMessage.objects.filter(is_active=True))
    return {'status_messages': status_messages}
