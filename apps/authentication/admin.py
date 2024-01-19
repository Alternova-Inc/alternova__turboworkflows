from django.contrib import admin

# Register your models here.
from apps.authentication.models.profile import Profile
from apps.authentication.models.company import Company
from apps.authentication.models.company_profile_set import CompanyProfileSet
from apps.authentication.models.role import Role

class CompanyProfileSetInline(admin.TabularInline):
    model = CompanyProfileSet
    extra = 0  # number of extra forms to display

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name')
    inlines = [CompanyProfileSetInline]

    def user_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name')

class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'role_name', 'company')
    filter_horizontal = ('workflows',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Role, RoleAdmin)
