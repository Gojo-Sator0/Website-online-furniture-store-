from django.contrib import admin
from carts.admin import CartTabAdmin
from users.models import User
from orders.admin import OrderTabulareAdmin
# Register your models here.

# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    search_fields = ['first_name', 'last_name', 'email']


    inlines = [CartTabAdmin, OrderTabulareAdmin]