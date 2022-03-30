from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse


class Address(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)

  address_type = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  state = models.CharField(max_length=255)
  postal_code = models.CharField(max_length=20)

  class Meta:
    unique_together = ('user', 'address_type',)

class Product(models.Model):
  name = models.CharField(max_length=256) 
  slug = models.CharField(max_length=256)
  description = models.TextField()  
  price = models.DecimalField(max_digits=7, decimal_places=2)

  def save(self, *args, **kwargs):
    self.slug = slugify(self.name)
    super(Product, self).save(*args, **kwargs)

  def get_url(self):
  	return reverse('product_detail', args=(self.merchant_set.all()[0].slug, self.slug, self.id))


class Merchant(models.Model):
  name = models.CharField(max_length=256)
  slug = models.CharField(max_length=256)
  products = models.ManyToManyField(Product)  

  def save(self, *args, **kwargs):
    self.slug = slugify(self.name)
    super(Merchant, self).save(*args, **kwargs)

class Order(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  products = models.ManyToManyField(Product)
  order_date = models.DateTimeField(auto_now_add=True)
  address = models.ForeignKey(Address,on_delete=models.CASCADE)

class Cart(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  products = models.ManyToManyField(Product)
