from django.shortcuts import render
from django.http import HttpResponse
# importing the Product Class for operation
from .models import Product, Contact, Order, OrderUpdate
import json
import math
# Create your views here.
def index(request):
    # print(Product.objects.all())
    all_product = []
    catprods = Product.objects.values('category','id')  
    categories = {item['category'] for item in catprods}
    for  category in categories:
        product_list = Product.objects.filter(category = category).order_by('product_pub_date')[::-1]
        n = len(product_list)
        nslides = n//4 + math.ceil(n/4 - n//4) 
        all_product.append(product_list)
    dict1 = {'all_products': all_product}
    return render(request,'shop/index.html', dict1)

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
    if(request.method == "POST"):
        # Fetching Data from the tracker form
        order_id = request.POST.get('order-id')
        email = request.POST.get('email')
        try:
            # Searching gor the order in the "ORDER" table
            order = Order.objects.filter(order_id = order_id, email = email)
            order_list = [item.items_json for item in order]
            if(len(order) > 0):
                update = OrderUpdate.objects.filter(order_id = order_id)
                updates = []
                for item in update:
                    updates.append({'text':item.order_desc, 'time':item.timeStamp})
                response = json.dumps([updates, order_list], default=str)
                return HttpResponse(response)
            else:
                pass
        except Exception as e:
            print(f"Error: {e}")    
    return render(request,'shop/tracker.html')

def search(request):
    return render(request,'shop/s.html')

def productView(request, proId):
    product_selected = Product.objects.filter(id = proId)
    return render(request,'shop/productView.html',{'product':product_selected})

def checkout(request):
    delivered_message = ""
    order_id = ""
    # Form to fill up "ORDERS" Table
    # Ordering the products with info
    if(request.method == 'POST'):
        items_json = request.POST.get('items_json')
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        order = Order(items_json = items_json,name = name, email = email,address=address, phone = phone,city = city, state=state, zip_code = zip_code)
        order.save()
        update = OrderUpdate(order_id = order.order_id, order_desc="Your update has been placed")
        update.save()
        delivered_message = "Message Delivered"
        order_id = order.order_id

    return render(request,'shop/checkout.html', {"message":delivered_message, "order_id":order_id})