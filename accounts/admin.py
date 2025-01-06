from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import UserModel, PatientProfile


class UserAdmin(BaseUserAdmin):
    list_display = (
        "email",
        "username",
        "first_name",
        "last_name",
        "is_admin",
        "is_nurse",
    )
    list_filter = ("is_admin", "is_nurse")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "first_name",
                    "middle_name",
                    "last_name",
                    "password",
                    # "is_admin",
                    # "is_nurse",
                )
            },
        ),
        ("Email", {"fields": ("email",)}),
        (
            "Personal info",
            {
                "fields": (
                    "age",
                    "gender",
                    "phone_number",
                    "address",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_nurse",
                    "is_admin",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "first_name",
                    "middle_name",
                    "last_name",
                    "password1",
                    "password2",
                    "is_admin",
                    "is_nurse",
                ),
            },
        ),
    )
    search_fields = ("email", "username", "first_name", "middle_name", "last_name")


admin.site.register(UserModel, UserAdmin)
admin.site.register(PatientProfile)
