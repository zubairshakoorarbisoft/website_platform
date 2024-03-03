from django.db import models
from django.utils import timezone


class Technology(models.Model):
    technology_name= models.CharField(max_length=200, null=False)
    technology_image= models.FileField(upload_to= 'media/uploads' , default='', blank=True)
    technology_discription= models.CharField(max_length=500, null=True)
    content= models.CharField(max_length=1000)
    technology_image= models.FileField(upload_to= 'media/uploads', default='' , blank=True)
    url= models.SlugField(max_length=200, default="")

