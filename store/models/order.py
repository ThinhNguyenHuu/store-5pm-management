from django.utils import timezone

from django.contrib.auth.models import User
from djongo import models
from store.models import Item

ORDER_STATUS = (
    ('pending', 'Pending'),
    ('confirmed', 'Confirmed'),
    ('delivered', 'Delivered'),
    ('cancelled', 'Cancelled'),
)


class Order(models.Model):
    _id = models.ObjectIdField()
    customer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    note = models.TextField(blank=True)
    total_price = models.FloatField(default=0)
    status = models.CharField(choices=ORDER_STATUS, default='pending', max_length=30)
    created_by = models.ForeignKey(User, db_column='user', on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(default=timezone.now)


class OrderDetail(models.Model):
    _id = models.ObjectIdField()
    order = models.ForeignKey(Order, db_column='order', on_delete=models.CASCADE, related_name='details')
    item = models.ForeignKey(Item, db_column='item', on_delete=models.CASCADE, related_name='order_details')
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.FloatField(default=0)
    discount = models.FloatField(default=0)
