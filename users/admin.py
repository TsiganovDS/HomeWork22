from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('avatar', 'phone_number', 'country')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'avatar', 'phone_number', 'country'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'phone_number', 'country', 'is_staff')

    search_fields = ('email', 'first_name', 'last_name', 'phone_number')
    ordering = ('email',)
