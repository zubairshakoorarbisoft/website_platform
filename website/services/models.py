from django.db import models
from django.utils import timezone


class Service(models.Model):
    service_name= models.CharField(max_length=200, null=False)
    service_image= models.FileField(upload_to= 'media/uploads' , default='', blank=True)
    service_discription= models.CharField(max_length=500, blank=True)
    content= models.CharField(max_length=2000, blank=True)
    cover_image= models.FileField(upload_to= 'media/uploads', default='' , blank=True)
    url= models.SlugField(max_length=200, default="")
    def __str__(self):
        return self.service_name


class SubServices(models.Model):
    name= models.CharField(max_length=200, null=False)
    category = models.ForeignKey(Service, on_delete=models.CASCADE)
    disc= models.CharField(max_length=500, blank=True)
    content= models.CharField(max_length=2000, blank=True)
    image= models.FileField(upload_to= 'media/uploads' , default='', blank=True)
    def __str__(self):
        return self.name
    
    