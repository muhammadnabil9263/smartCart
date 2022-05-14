from itertools import product
from rest_framework import serializers
from .models import OrderItem, Product , Order
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
     class Meta:
        model = User 
        fields = [ 'username','password'  ]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = ['id', 'name', 'description', 'price','Quantity','barcode']


class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(read_only= True )
    class Meta:
        model = OrderItem 
        fields = ['product','quantity']

class OrderSerializer(serializers.ModelSerializer):
    orderItems = OrderItemSerializer(many=True,read_only= True )
    customer = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Order 
        fields = ['id','customer','cart','date_ordered','complete','orderItems']
