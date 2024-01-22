from apps.defaults.models.base_model import BaseModel
from django.db import models

class StatusMessage(BaseModel):
    """
    - This is used to show status messages on the first page of the django admin.
    - Thhis should be used to show important maintenance messages to the user.
    """

    status_message_name = models.CharField(max_length=40, help_text="Status Message Name", verbose_name="Name")
    contentame = models.CharField(max_length=300, help_text="What the user should be informed about")

    class Meta:
        verbose_name = 'Status Message'
        verbose_name_plural = 'Status Messages'

    def __str__(self):
        return f"{self.status_message_name}"
    
    