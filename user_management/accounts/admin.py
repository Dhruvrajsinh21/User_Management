from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('id', 'name', 'email', 'phone_number', 'is_active', 'is_super_admin')
    # Fields to filter in the admin list view
    list_filter = ('is_active', 'is_super_admin')
    # Fields to search in the admin list view
    search_fields = ('name', 'email', 'phone_number')
    # Fields to sort in the admin list view
    ordering = ('-id',)
    # Fields to display in the edit view
    fieldsets = (
        (None, {'fields': ('name', 'email', 'password', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_super_admin')}),
    )
    # Fields to display when creating a new user in admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'password', 'phone_number', 'is_active', 'is_super_admin'),
        }),
    )
