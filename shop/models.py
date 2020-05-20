from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    product_description = models.CharField(max_length=300)
    category = models.CharField(max_length=30, default='')
    sub_category = models.CharField(max_length=30, default='')
    price = models.IntegerField(default=0) 
    image = models.ImageField(upload_to="shop/images", default='')
    product_pub_date = models.DateField() 

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msgId = models.AutoField(primary_key = True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30, default="")
    phone = models.CharField(max_length=12, default="")
    message = models.CharField(max_length=30, default="") 

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key = True)
    items_json = models.CharField(max_length=6000)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key = True)
    order_id = models.IntegerField()
    order_desc = models.CharField(max_length=5000)
    timeStamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.order_desc[0:10] + "..."