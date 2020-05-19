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
