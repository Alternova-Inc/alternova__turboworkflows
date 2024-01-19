from django.contrib import admin

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
