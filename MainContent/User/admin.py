from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from MainContent.User.models import User

# Register your models here.
class ManagerAdminUser(UserAdmin):
    """inlines = (Inline_Participantes,)
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('tipo', 'cargo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('carnet',)}),
    )
    search_fields = ("username", "email", "first_name", "last_name", "carnet")
    list_filter = ("is_superuser", "user_permissions", "is_active",
                      "is_staff", "tipo", "cargo", "last_login")"""
    pass

admin.site.register(User)