from django.db import models
import os
from django.utils import timezone


class Product(models.Model):
    #Hero Section
    product_name= models.CharField(max_length=200, null=False)
    url= models.SlugField(max_length=200, blank=False)
    product_image= models.FileField(upload_to= 'media/uploads' , default='', blank=True)
    h1= models.CharField(max_length=200 , default='')
    product_discription= models.CharField(max_length=500, null=True)
    #Product Development Section
    h2= models.CharField(max_length=200, null=True)
    content= models.CharField(max_length=500, null=True)
    process_1= models.CharField(max_length=200, null=True)
    process_1_disc= models.CharField(max_length=500, null=True)
    process_2= models.CharField(max_length=200, null=True)
    process_2_disc= models.CharField(max_length=500, null=True)
    process_3= models.CharField(max_length=200, null=True)
    process_3_disc= models.CharField(max_length=500, null=True)
    process_4= models.CharField(max_length=200, null=True)
    process_4_disc= models.CharField(max_length=500, null=True)
    # Product Usage Section
    usage_1= models.CharField(max_length=200, null=True)
    usage_1_disc= models.CharField(max_length=500, null=True)
    usage_2= models.CharField(max_length=200, null=True)
    usage_2_disc= models.CharField(max_length=500, null=True)
    usage_3= models.CharField(max_length=200, null=True)
    usage_3_disc= models.CharField(max_length=500, null=True)
    usage_4= models.CharField(max_length=200, null=True)
    usage_4_disc= models.CharField(max_length=500, null=True)
    # Backend Technologies Used in the Product
    dotnet = models.BooleanField()
    java = models.BooleanField()
    python = models.BooleanField()
    php = models.BooleanField()
    nodejs = models.BooleanField()
    # Front end technologies
    html = models.BooleanField()
    css = models.BooleanField()
    javascript = models.BooleanField()
    react = models.BooleanField()
    vue = models.BooleanField()
    angular = models.BooleanField()
    #cloud technologies
    aws = models.BooleanField()
    azure = models.BooleanField()
    googlecloud = models.BooleanField()
    #mobile applications technologies
    ios = models.BooleanField()
    android = models.BooleanField()
    reactnative = models.BooleanField()
    flutter = models.BooleanField()
    kotlin = models.BooleanField()
    #database technologies
    sqlserver = models.BooleanField()
    mysql = models.BooleanField()
    postgres = models.BooleanField()
    mongodb = models.BooleanField()
    #payement gateways
    paypal = models.BooleanField()
    stripe = models.BooleanField()
    visa = models.BooleanField()
    gpay = models.BooleanField()

    cover_image= models.FileField(upload_to= 'media/uploads', default='' , blank=True)
    
