from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from ..forms import UserCreationForm, UserChangeForm
from ..models import User


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('national_code', 'is_superuser', 'is_active', 'is_staff',)
    list_filter = ('national_code', 'is_superuser', 'is_active', 'is_staff', "user_permissions",)
    fieldsets = (
        ("INFO", {'fields': (
            'national_code', 'phone_number', 'password', 'profile', 'is_superuser', 'is_active', 'is_staff',)}),
        ("AUTHENTICATION AND AUTHORIZATION", {'fields': ("groups", "user_permissions",)}),

    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('national_code', 'phone_number', 'password1', 'password2',),
        }),
    )
    search_fields = ('national_code',)
    ordering = ('national_code',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
