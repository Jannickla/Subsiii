from django.contrib import admin
from .models import Item, Box, OrderItem, OrderBox, Order


admin.site.register(Item)
admin.site.register(Box)
admin.site.register(OrderItem)
admin.site.register(OrderBox)
admin.site.register(Order)
