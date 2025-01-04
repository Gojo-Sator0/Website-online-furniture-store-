from django.shortcuts import render

# Create your views here.

def cart_add(request, product_id):
    return render(request, 'carts/cart_add.html')

def cart_chance(request, product_id):
    return render(request, 'carts/cart_chance.html')

def cart_remove(request, product_id):  
    return render(request, 'carts/cart_remove.html')