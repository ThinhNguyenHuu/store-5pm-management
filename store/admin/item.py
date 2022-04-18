from django.contrib import admin


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        '_id', 'name', 'type', 'feature', 'size', 'color', 'price', 'quantity',
    )
    list_filter = ('type', 'feature')
    search_fields = ['name', 'feature']
