from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token




class Product(models.Model):
  name = models.CharField(max_length=256) 
  description = models.TextField()  
  price = models.DecimalField(max_digits=7, decimal_places=2)
  Quantity = models.IntegerField(default=0) 
  barcode = models.CharField(max_length=256,blank=True,null=False) 

  def __str__(self):
      return self.name


class Cart (models.Model):
    occupied = models.BooleanField(default=False)
      
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)
    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="product", null=True)
    order = models.ForeignKey(Order, related_name="orderItems",on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)





@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)