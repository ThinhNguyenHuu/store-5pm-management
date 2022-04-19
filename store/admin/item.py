from bson import ObjectId
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import path
from django.urls import reverse
from django.utils.html import format_html
from django import forms
from common.admin import BaseAdmin
from store.models import ImportLog
from store.models import Item


class ImportItemForm(forms.Form):
    quantity = forms.IntegerField()

    def process(self, user, item):
        quantity = self.cleaned_data['quantity']
        if quantity <= 0:
            return False, None
        item.quantity = item.quantity + quantity
        item.save(update_fields=['quantity'])
        log = ImportLog.objects.create(
            item=item,
            user=user,
            quantity=quantity,
        )
        return True, log


class ItemAdmin(BaseAdmin):
    list_display = (
        'id', 'name', 'type', 'feature', 'size', 'color', 'price', 'quantity', 'import_items',
    )
    list_filter = ('type', 'feature')
    search_fields = ['id', 'name', 'feature']

    def has_change_permission(self, request, obj=None):
        return True

    def import_items(self, item):
        return format_html(
            '<a href="{url}">Import</a>',
            url=reverse('admin:store_item_import_items', args=(item._id,)),
        )

    def get_urls(self):
        info = self.model._meta.app_label, self.model._meta.model_name
        urlpatterns = [
            path(
                '<path:object_id>/import/',
                self.admin_site.admin_view(self.import_items_view),
                name='%s_%s_import_items' % info,
            ),
        ]
        urls = super(ItemAdmin, self).get_urls()
        return urlpatterns + urls

    def import_items_view(self, request, object_id, **kwargs):
        item = Item.objects.get(_id=ObjectId(object_id))

        if request.method == 'GET':
            form = ImportItemForm(initial={'quantity': 0})
            context = {
                'form': form,
                'item': item,
            }
            return render(request, 'item/import_item.html', context)

        form = ImportItemForm(request.POST)
        form.is_valid()
        success, log = form.process(user=request.user, item=item)

        if success:
            messages.success(request, f'Import item {item.name} success with quantity {log.quantity}')
            return redirect(reverse('admin:store_item_changelist'))
        else:
            messages.error(request, f'Quantity cannot be negative')
            form = ImportItemForm(initial={'quantity': 0})
            context = {
                'form': form,
                'item': item,
            }
            return render(request, 'item/import_item.html', context)
