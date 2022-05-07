from itertools import product
from django.http import JsonResponse
from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here. 
# List all Prdoucts
   
@csrf_exempt
def products_list(request):   
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return JsonResponse(serializer.data, safe=False)
