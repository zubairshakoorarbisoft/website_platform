from django.db import models
import os
from django.utils import timezone


class Product(models.Model):
    product_name= models.CharField(max_length=200, null=False)
    product_image= models.FileField(upload_to= 'media/uploads' , default='', blank=True)
    product_discription= models.CharField(max_length=500, null=True)
    content= models.CharField(max_length=1000)
    cover_image= models.FileField(upload_to= 'media/uploads', default='' , blank=True)
    url= models.SlugField(max_length=200, blank=True)
