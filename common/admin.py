from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.auth.admin import UserAdmin as DjUserAdmin


class BaseAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return True

    def has_view_permission(self, request, obj=None):
        return True


class UserAdmin(DjUserAdmin, BaseAdmin):
    search_fields = ('username',)


class LogEntryAdmin(BaseAdmin):
    list_display = ('id', 'user', 'action_time', 'object_id', 'object_repr', 'action_flag')
    search_fields = ('user', 'action_flag', 'action_time')


admin.site.register(LogEntry, LogEntryAdmin)
