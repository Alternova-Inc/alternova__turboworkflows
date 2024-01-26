from django.db import models
from django.forms import ValidationError
from apps.authentication.models.company import Company
from apps.defaults.models.base_model import BaseModel


class UserFormField(BaseModel):
    """
    - Fields that compose a User Form
    """

    TYPE_CHOICES = [
        ('ShortText', 'Short Text'),
        ('Numeric', 'Numeric'),
        ('LongText', 'Long Text'),
        ('MultipleSelection', 'Multiple Selection'),
        ('SingleSelection', 'Single Selection'),
        ('Date', 'Date'),
        ('Boolean', 'Boolean'),
    ]

    code = models.CharField(max_length=20, unique=True, help_text="Internal code - Must be unique")
    public_name = models.CharField(max_length=40, help_text="Name shown to the user")
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, help_text="Type of the form field")
    choices = models.CharField(max_length=250, help_text="Comma-separated values. 250 characters max. Required for Multiple Selection or Single Selection type.", blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'User Form Field'
        verbose_name_plural = 'User Form Fields'

    def __str__(self):
        return f'{self.code} - {self.public_name} - {self.company}'

    def clean(self):
        if self.type in ['MultipleSelection', 'SingleSelection']:
            if not self.choices:
                raise ValidationError("Choices are required for Multiple Selection or Single Selection type.")
        else:
            self.choices = ''  # Clear choices for other types

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
        
    