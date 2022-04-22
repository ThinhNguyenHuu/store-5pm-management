from bson import ObjectId
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.auth.admin import UserAdmin as DjUserAdmin
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError
from django.forms import ModelChoiceField


class CustomModelChoiceField(ModelChoiceField):
    def clean(self, value):
        try:
            return self.queryset.get(pk=value)
        except ObjectDoesNotExist:
            pass
        try:
            return self.queryset.get(pk=ObjectId(value))
        except ObjectDoesNotExist:
            raise ValidationError(self.error_messages['invalid_choice'], code='invalid_choice')


class BaseAdminInline(admin.TabularInline):
    def has_module_permission(self, request):
        return True

    def has_view_permission(self, request, obj=None):
        return True


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
