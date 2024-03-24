from django.db import models
from django.utils import timezone


class Technology(models.Model):
     #Hero Section
    technology_name= models.CharField(max_length=200, null=False)
    url= models.SlugField(max_length=200, blank=False)
    technology_image= models.FileField(upload_to= 'media/uploads' , default='', blank=True)
    h1= models.CharField(max_length=200 , default='')
    technology_discription= models.CharField(max_length=500, null=True)
    #Section 2:
    h2= models.CharField(max_length=200, null=True)
    content= models.CharField(max_length=500, null=True)
    benefit_1= models.CharField(max_length=200, null=True)
    benefit_1_disc= models.CharField(max_length=500, null=True)
    benefit_2= models.CharField(max_length=200, null=True)
    benefit_2_disc= models.CharField(max_length=500, null=True)
    benefit_3= models.CharField(max_length=200, null=True)
    benefit_3_disc= models.CharField(max_length=500, null=True)
    benefit_4= models.CharField(max_length=200, null=True)
    benefit_4_disc= models.CharField(max_length=500, null=True)    
    # Technology Usage Section
    usage_1= models.CharField(max_length=200, null=True)
    usage_1_disc= models.CharField(max_length=500, null=True)
    usage_2= models.CharField(max_length=200, null=True)
    usage_2_disc= models.CharField(max_length=500, null=True)
    usage_3= models.CharField(max_length=200, null=True)
    usage_3_disc= models.CharField(max_length=500, null=True)
    usage_4= models.CharField(max_length=200, null=True)
    usage_4_disc= models.CharField(max_length=500, null=True)
    