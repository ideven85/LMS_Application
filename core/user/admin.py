from django.contrib import admin

from core.user.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_active', 'is_staff', 'first_name', 'last_name']

