from django.contrib import admin

from store import models
from store.admin.item import ItemAdmin

admin.site.register(models.Item, ItemAdmin)
