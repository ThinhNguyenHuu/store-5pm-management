from django.contrib import admin

from store import models
from store.admin.item import ItemAdmin
from store.admin.import_log import ImportLogAdmin
from store.admin.order import OrderAdmin

admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.ImportLog, ImportLogAdmin)
admin.site.register(models.Order, OrderAdmin)
