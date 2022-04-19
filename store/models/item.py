from djongo import models


ITEM_TYPE = (
    ('tshirt', 'T-Shirt'),
)

ITEM_FEATURE = (
    ('no_hookups', 'No Hookups'),
)

ITEM_SIZE = (
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
)

ITEM_COLOR = (
    ('white', 'White'),
    ('black', 'Black'),
)


class Item(models.Model):
    _id = models.ObjectIdField()
    id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    type = models.CharField(choices=ITEM_TYPE, default='tshirt', max_length=30)
    feature = models.CharField(choices=ITEM_FEATURE, default='no_hookups', max_length=50)
    size = models.CharField(choices=ITEM_SIZE, default='M', max_length=8)
    color = models.CharField(choices=ITEM_COLOR, default='white', max_length=50)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.id} | {self.name}'
