from django.contrib.auth.models import User
from django.utils import timezone
from djongo import models

from store.models import Item


class ImportLog(models.Model):
    _id = models.ObjectIdField()
    item = models.ForeignKey(Item, db_column='item', on_delete=models.CASCADE, related_name='import_logs')
    user = models.ForeignKey(User, db_column='user', on_delete=models.CASCADE, related_name='import_logs')
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('created_at',)
