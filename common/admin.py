from django.contrib import admin
from django.contrib.admin.models import LogEntry


class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'action_time', 'object_id', 'object_repr', 'action_flag')
    search_fields = ('user', 'action_flag', 'action_time')


admin.site.register(LogEntry, LogEntryAdmin)
