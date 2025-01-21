from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_number', 'is_active', 'is_super_admin')
    list_filter = ('is_active', 'is_super_admin')
    search_fields = ('name', 'email', 'phone_number')
    ordering = ('-id',)
    fieldsets = (
        (None, {'fields': ('name', 'email', 'password', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_super_admin')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'password', 'phone_number', 'is_active', 'is_super_admin'),
        }),
    )
