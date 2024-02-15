from django.contrib import admin
from apps.authentication.models.company_department import CompanyDepartment
from apps.authentication.models.company_position import CompanyPosition

# Register your models here.
from apps.authentication.models.profile import Profile
from apps.authentication.models.company import Company
from apps.authentication.models.company_profile_set import CompanyProfileSet
from apps.authentication.models.role import Role
from apps.defaults.admin import BaseModelAdmin

class CompanyProfileSetInline(admin.TabularInline):
    model = CompanyProfileSet
    extra = 0  # number of extra forms to display
    fk_name = 'profile'

class ProfileAdmin(BaseModelAdmin):
    list_extend = ('user_name', 'user_email', 'user_username', 'user_is_staff', 'user_is_superuser', 'user_last_login',)
    search_fields_extend = ('user__first_name', 'user__last_name', 'user__email', 'user__username',)
    inlines = [CompanyProfileSetInline]

    def user_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    
    def user_email(self, obj):
        return obj.user.email

    def user_username(self, obj):
        return obj.user.username

    def user_is_staff(self, obj):
        return obj.user.is_staff

    def user_is_superuser(self, obj):
        return obj.user.is_superuser

    def user_last_login(self, obj):
        return obj.user.last_login


class CompanyAdmin(BaseModelAdmin):
    list_extend = ('company_name',)
    search_fields_extend = ('company_name',)

    
class RoleAdmin(BaseModelAdmin):
    list_extend = ('role_name', 'company',)
    search_fields_extend = ('role_name', 'company__company_name',)
    filter_horizontal = ('workflows',)


class CompanyDepartmentAdmin(BaseModelAdmin):
    list_extend = ('department_name', 'company',)
    search_fields_extend = ('department_name', 'company__company_name',)


class CompanyPositionAdmin(BaseModelAdmin):
    list_extend = ('position_name', 'is_approver', 'company',)
    search_fields_extend = ('position_name', 'company__company_name',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(CompanyDepartment, CompanyDepartmentAdmin)
admin.site.register(CompanyPosition, CompanyPositionAdmin)
