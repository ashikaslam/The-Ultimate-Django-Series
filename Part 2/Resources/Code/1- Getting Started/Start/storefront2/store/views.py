from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from . serializers import ProductSerializer


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
            queryset =Product.objects.all().select_related("collection")
        #   queryset =Product.objects.select_related("collection").all() #these are same
            serializer = ProductSerializer(queryset,many=True,context={'request': request})
            return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('ok')



@api_view(['GET', 'PUT'])
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    



@api_view()
def collection_detail(request, pk):
    return Response('ok')