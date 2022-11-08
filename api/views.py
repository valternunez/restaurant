from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Order
from .serializers import OrderSerializer
from django.views.generic.list import ListView
import requests
from django.shortcuts import render

@api_view(['GET', 'POST'])
def order_list(request):
    if request.method == 'GET':
        orders = Order.objects.all().order_by("created_at")
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
       
    
    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def order_detail(request, id):
    try:
        order = Order.objects.get(pk=id)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def client_order_list(request):
    response = requests.get("http://localhost:8000/api/")
    orders = response.json()
    if request.htmx:
        return render(request, "orderlist.html", {'orders': orders})
    else:
        return render(request, "base.html", {'orders': orders})

def client_order_detail(request, id):
    response = requests.get(f"http://localhost:8000/api/{id}")
    order = response.json()
    # return render(request, "orderdetail.html", {'orders': orders})
    if request.htmx:
        return render(request, "orderdetail.html", {'order': order})
    else:
        return render(request, "base_orderdetail.html", {'order': order})
