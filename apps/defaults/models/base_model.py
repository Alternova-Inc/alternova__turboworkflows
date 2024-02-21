import uuid

from django.db import models


class BaseModel(models.Model):
    """
    Base model for all models in the application.
    """

    id = models.CharField(
        primary_key=True, unique=True, default="Empty", editable=False, max_length=255
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        Overrides the save method to generate a unique ID before saving the model.
        """
        if self._state.adding:
            self.id = str(uuid.uuid4())
        super().save(*args, **kwargs)

    def disable(self):
        """
        Disables the model by setting the 'is_active' field to False and saving the model.
        """
        self.is_active = False
        self.save()
        