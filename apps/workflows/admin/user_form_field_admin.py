from django.contrib import admin

from apps.defaults.admin import BaseModelAdmin
from apps.workflows.models.user_form_field import UserFormField

class UserFormFieldAdmin(BaseModelAdmin):
    list_extend = ('code', 'public_name', 'type', 'company_name',)
    search_fields_extend = ('public_name', 'company__company_name',)
    list_filter = ('company',)
    
    def company_name(self, obj):
        return f"{obj.company.company_name}"
    
admin.site.register(UserFormField, UserFormFieldAdmin)