from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile, Address


# Register your models here.
class AddressInline(admin.TabularInline):
    """Display user addresses inline on the user admin page"""
    model = Address
    extra = 0 # Don't show empty forms by default
    fields = ('address_type', 'full_name', 'address_line_1', 'city', 'postcode')
    readonly_fields = ('created_at',)


class UserProfileInline(admin.StackedInline):
    """Display user profile information inline on the user admin page"""
    model = UserProfile
    can_delete = False # Prevent deletion of profile through user admin
    verbose_name_plural = 'Profile'


class UserAdmin(BaseUserAdmin):
    """
    Enhanced user admin that includes profile and address information.
    Extends Django's default UserAdmin to show related data.
    """
    inlines = (UserProfileInline,)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    """
    Admin interface for managing user addresses.
    Provides filtering and search for easy address management.
    """
    list_display = ('full_name', 'user', 'address_type', 'city', 'country', 'created_at')
    list_filter = ('address_type', 'country', 'created_at')
    search_fields = ('full_name', 'user__username', 'city', 'postcode')
    ordering = ('-created_at',) # Show newest addresses first


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin interface for user profiles.
    Shows profile information and allows setting default addresses.
    """
    list_display = ('user', 'full_name', 'phone_number', 'default_address')
    search_fields = ('user__username', 'first_name', 'last_name')
    list_filter = ('created_at',)


# Unregister the default User admin for custom admin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)