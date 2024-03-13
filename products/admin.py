from django.contrib import admin

from products.models import Product, ProductCategory, Basket

admin.site.register(ProductCategory)
# admin.site.register(Product)
admin.site.register(Basket)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
    fields = ('name', 'image', 'description', 'short_description', 'price', 'quantity', 'category')
    readonly_fields = ('image',)
