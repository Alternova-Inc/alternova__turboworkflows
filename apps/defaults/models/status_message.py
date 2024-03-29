from django.forms import ValidationError
from apps.defaults.models.base_model import BaseModel
from django.db import models

class StatusMessage(BaseModel):
    """
    - This is used to show status messages on the first page of the django admin.
    - Thhis should be used to show important maintenance messages to the user.
    - By default, the status message is not active.
    - Only one message can be active at a time.
    """

    status_message_name = models.CharField(max_length=40, help_text="Status Message Name", verbose_name="Name")
    content = models.CharField(max_length=300, help_text="What the user should be informed about")

    class Meta:
        verbose_name = 'Status Message'
        verbose_name_plural = 'Status Messages'

    def __str__(self):
        return f"{self.status_message_name}"
    
    def clean(self):
        if self.is_active and StatusMessage.objects.filter(is_active=True).exclude(pk=self.pk).exists():
            raise ValidationError("An active Status Message already exists.")

    def save(self, *args, **kwargs):
        self.full_clean()
        if self._state.adding: # if object is new, not from the DB
            self.is_active = False
        super().save(*args, **kwargs)
        