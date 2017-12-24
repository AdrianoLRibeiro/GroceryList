from django.contrib import admin

from .models import Department, Product, Product_Pss, Brand, Item, Market, Purchase


class ProductAdmin(admin.ModelAdmin):
    model = Product
    exclude = ['avg_price', 'max_price', 'min_price']

class ItemAdmin(admin.ModelAdmin):
    readonly_fields = ['sub_total']

class PurchaseAdmin(admin.ModelAdmin):
    mode = Purchase
    list_display = ["date",]
    readonly_fields = ['value']

admin.site.register(Product, ProductAdmin)
admin.site.register(Department)
admin.site.register(Brand)
admin.site.register(Item, ItemAdmin)
admin.site.register(Market)
admin.site.register(Purchase, PurchaseAdmin)