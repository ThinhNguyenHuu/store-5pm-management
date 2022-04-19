from django.conf import settings
from django.utils import timezone
from djongo import models


class ImportLog(models.Model):
    _id = models.ObjectIdField()
    item = models.ForeignKey('store.Item', on_delete=models.CASCADE, related_name='import_logs')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='import_logs')
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('created_at',)
