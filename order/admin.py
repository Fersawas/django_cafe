from django.contrib import admin
from order.models import Order, OrderDetail, Table, Food


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'id')  


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'all_price', 'table', 'get_food')
    readonly_fields = ['all_price', ]
    list_filter = ('table',)

    def get_food(self, obj):
        return ', '.join([food.title for food in obj.food.all()])
    
    get_food.short_description = 'Блюда'


@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'food', 'quantity', 'price')
    readonly_fields = ['price']
    list_filter = ('order', 'food')


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    search_fields = ('title',)