from django.db import models
from homepage.models import UserID
# Create your models here.
class Product (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=5000, null=True, blank=True)
    price = models.FloatField()
    image = models.ImageField(max_length = 500,null=True, blank=True, upload_to = 'images')
    is_pdf = models.BooleanField(default=False)
    is_physical = models.BooleanField(default=False)
    is_ebook = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.id}, {self.name}, {self.author}, {self.description}";
class Review(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserID, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.CharField(max_length=500)
    
    def __str__(self):
        return f"{self.user}, {self.product}, {self.review}"
    

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(UserID, on_delete=models.CASCADE, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    
    def __str__(self):
        return f"{self.customer}, {self.date_ordered}. {self.complete}"
    
    @property
    def cart_total (self):
        orderitems = self.orderitem_set.all()
        total =  sum([item.get_total for item in orderitems])
        return total
    
    @property
    def cart_count(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete = models.CASCADE, null=True)
    quantity = models.IntegerField(null=True, default=0, blank = 0)
    date_added = models.DateTimeField(null=True, auto_now_add=True)
    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    
    def __str__(self):
        return f"{self.product}, {self.order}, {self.quantity}, {self.date_added}"