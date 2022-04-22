from common.admin import BaseAdmin


class ImportLogAdmin(BaseAdmin):
    list_display = (
        'item', 'user', 'quantity', 'created_at',
    )
    list_filter = ('item', 'user')
    search_fields = ['item', 'user']
    autocomplete_fields = ['item', 'user']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return True

    def delete_model(self, request, obj):
        item = obj.item
        item.quantity = item.quantity - obj.quantity
        item.save(update_fields=['quantity'])
        super().delete_model(request, obj)
