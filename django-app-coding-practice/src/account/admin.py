from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import Account

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'last_login', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')
    filter_horizontal = ()
    list_filter = ()

admin.site.register(Account, AccountAdmin)
