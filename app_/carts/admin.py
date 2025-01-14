from django.contrib import admin
from carts.models import Cart
# Register your models here.

# admin.site.register(Cart)

class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = 'product', 'qty', 'created_timestamp'
    search_fields = 'product__name','qty','created_timestamp'
    readonly_fields = ('created_timestamp',)
    extra = 1

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user_display', 'product_display', 'qty', 'created_timestamp',]
    list_filter = ['created_timestamp', 'user', 'product__name',]

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return 'Анонимный пользователь'

    def product_display(self, obj):
        return str(obj.product.name)