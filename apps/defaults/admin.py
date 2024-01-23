from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter
from apps.defaults.models.status_message import StatusMessage

# Register your models here.
class BaseModelAdmin(admin.ModelAdmin):
    """
    BaseModelAdmin is a base class for Django admin interfaces.
    
    It sets default values for list_display, search_fields, and ordering. 
    Subclasses can extend list_display and search_fields by defining list_extend and search_fields_extend respectively.
    """

    list_extend = ()
    search_fields_extend = ()
    ordering = ('-updated_at',)

    def __init__(self, model, admin_site):
        self.list_display = ['id'] + list(self.list_extend) + ['is_active', 'created_at', 'updated_at']
        self.search_fields = ['id'] + list(self.search_fields_extend)
        super().__init__(model, admin_site)


class BasePolymorphicParentModelAdmin(PolymorphicParentModelAdmin):
    """
    BaseModelAdmin is a base class for Django admin interfaces.
    
    It sets default values for list_display, search_fields, and ordering. 
    Subclasses can extend list_display and search_fields by defining list_extend and search_fields_extend respectively.
    """

    list_extend = ()
    search_fields_extend = ()
    ordering = ('-updated_at',)
    list_filter = (PolymorphicChildModelFilter,)

    def __init__(self, model, admin_site):
        self.list_display = ['id'] + list(self.list_extend) + ['is_active', 'created_at', 'updated_at']
        self.search_fields = ['id'] + list(self.search_fields_extend)
        super().__init__(model, admin_site)



# class BasePolymorphicChildModelAdmin(PolymorphicChildModelAdmin):
#     """ Base admin class for all child models """
#     base_model = ModelA  # Optional, explicitly set here.

#     # By using these `base_...` attributes instead of the regular ModelAdmin `form` and `fieldsets`,
#     # the additional fields of the child models are automatically added to the admin form.
#     base_form = ...
#     base_fieldsets = (
#         ...
#     )

class StatusMessageAdmin(BaseModelAdmin):
    list_extend = ('status_message_name', 'content',)
    search_fields_extend = ('status_message_name', 'content',)


admin.site.register(StatusMessage, StatusMessageAdmin)
