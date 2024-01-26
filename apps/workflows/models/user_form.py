from django.core.exceptions import ValidationError
from django.db import models
from apps.authentication.models.company import Company
from apps.defaults.models.base_model import BaseModel


class UserForm(BaseModel):
    """
    - Forms shown to users for users to fill in order to request something.
    """

    user_form_name = models.CharField(max_length=40, help_text="User Form Name", verbose_name="Name")
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'User Form'
        verbose_name_plural = 'User Forms'

    def __str__(self):
        return self.user_form_name
