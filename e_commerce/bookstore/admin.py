from django.contrib import admin
from bookstore.models import Product, Review, Order, OrderItem
# Register your models here.
class AdminProduct (admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'description', 'price',  'image', 'is_pdf', 'is_physical', 'is_ebook')

class AdminReview (admin.ModelAdmin):
    list_display = ('id','user', 'product', 'review')

class AdminOrder (admin.ModelAdmin):
    list_display = ('id','customer','date_ordered', 'complete')
    
class AdminOrderItem (admin.ModelAdmin):
    list_display = ('id','product','order', 'quantity', 'date_added')
admin.site.register(Product, AdminProduct)
admin.site.register(Review, AdminReview)
admin.site.register(Order, AdminOrder)
admin.site.register(OrderItem, AdminOrderItem)