from bson import Decimal128
from django.forms import ModelForm

from common.admin import BaseAdmin
from common.admin import BaseAdminInline
from common.admin import CustomModelChoiceField
from store.models import Item
from store.models import OrderDetail


class OrderDetailForm(ModelForm):
    item = CustomModelChoiceField(queryset=Item.objects.all())

    def save(self, commit=True):
        instance = super().save(commit=commit)
        item = instance.item
        item.quantity = item.quantity - instance.quantity
        item.save(update_fields=['quantity'])
        return instance


class OrderDetailInline(BaseAdminInline):
    model = OrderDetail
    form = OrderDetailForm
    fields = ('item', 'unit_price', 'discount', 'quantity')


class OrderAdmin(BaseAdmin):
    list_display = (
        'customer_name', 'phone_number', 'total_price', 'status', 'created_by', 'created_at',
    )
    list_filter = ('status', 'created_at')
    search_fields = ['customer_name', 'phone_number']
    readonly_fields = ('total_price', 'status', 'created_by')
    inlines = [
        OrderDetailInline
    ]

    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        order = form.instance
        total_price = 0
        for detail in order.details.all():
            total_price = total_price + detail.unit_price * detail.quantity
        order.total_price = total_price
        order.save()

    def delete_model(self, request, obj):
        for detail in obj.details.all():
            item = detail.item
            item.quantity = item.quantity + detail.quantity
            item.save(update_fields=['quantity'])
        super().delete_model(request, obj)
