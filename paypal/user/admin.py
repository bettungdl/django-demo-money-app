from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from user.models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'date_joined')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'wallet', 'id_user_stripe')}), # wallet
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'is_staff', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ('groups', 'user_permissions')
