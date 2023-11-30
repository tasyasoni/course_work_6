from django.contrib import admin
from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'country', 'email_verify',)
    list_filter = ('email',)
    search_fields = ('email',)