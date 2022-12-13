from django.db import models
from datetime import datetime
from django.contrib import messages

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.name

class seller(models.Model):
    name=models.CharField(max_length=200)
    seller_photo=models.ImageField(upload_to='photos/seller/%Y/%m/%d/')
    contact_no =models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category= models.ForeignKey(Category, related_name='lots', on_delete=models.CASCADE)
    seller = models.ForeignKey(seller,on_delete=models.DO_NOTHING)
    slug = models.SlugField(max_length=200,db_index=True)
    product_name=models.CharField(max_length=200,db_index=True)
    is_live=models.BooleanField(default=False)
    base_price=models.IntegerField(default=0.0)
    current_price=models.IntegerField(default=0.0)
    description=models.CharField(max_length=500)
    main_photo=models.ImageField(upload_to='product_img')
    photo1=models.ImageField(upload_to='product_img',blank=True)
    photo2=models.ImageField(upload_to='product_img',blank=True)
    is_trending=models.BooleanField(default=False)
    on_banner=models.BooleanField(default=False)
    year_published=models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.product_name
    


class Auction(models.Model):
    start =  models.DateTimeField(auto_now=False)
    curr_time =  models.DateTimeField(auto_now=False)
    item = models.OneToOneField(
    Product, on_delete=models.CASCADE, related_name="auction")
    def __str__(self):
        return self.item.product_name