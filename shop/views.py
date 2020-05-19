from django.shortcuts import render
from django.http import HttpResponse
# importing the Product Class for operation
from .models import Product, Contact
# Create your views here.
def index(request):
    # print(Product.objects.all())
    all_product = []
    catprods = Product.objects.values('category','id')  
    categories = {item['category'] for item in catprods}
    for  category in categories:
        product_list = Product.objects.filter(category = category).order_by('product_pub_date')[::-1]
        all_product.append(product_list)
    return render(request,'shop/index.html', {'products':all_product})

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    delivered_message = ""
    if(request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        Contact(name = name, email = email, phone = phone, message = message).save()
        delivered_message = "Message Delivered"
    return render(request,'shop/contact.html',{'delivered_message': delivered_message})

def tracker(request):
    return render(request,'shop/tracker.html')

def search(request):
    return render(request,'shop/s.html')

def productView(request, proId):
    product_selected = Product.objects.filter(id = proId)
    return render(request,'shop/productView.html',{'product':product_selected})

def checkout(request):
    return render(request,'shop/checkout.html')