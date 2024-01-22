from django.test import TestCase
from apps.defaults.models import StatusMessage


# Create your tests here.
class StatusMessageTestCase(TestCase):
    def test_is_active_default(self):
        # Create a new StatusMessage instance
        status_message = StatusMessage.objects.create(
            status_message_name="Test message",
            content="Test content"
        )

        # Check if is_active is False
        self.assertFalse(status_message.is_active)
        