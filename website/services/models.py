from django.db import models
from django.utils import timezone


class Service(models.Model):
    #Hero Section
    service_name= models.CharField(max_length=200, null=False)
    url= models.SlugField(max_length=200, blank=False)
    service_image= models.FileField(upload_to= 'media/uploads' , default='', blank=True)
    h1= models.CharField(max_length=200 , default='')
    service_discription= models.CharField(max_length=500, blank=True)

    h2= models.CharField(max_length=200, blank=True)
    content= models.CharField(max_length=500, blank=True)
    benefit_1= models.CharField(max_length=200, blank=True)
    benefit_1_disc= models.CharField(max_length=500, blank=True)
    benefit_2= models.CharField(max_length=200, blank=True)
    benefit_2_disc= models.CharField(max_length=500, blank=True)
    benefit_3= models.CharField(max_length=200, blank=True)
    benefit_3_disc= models.CharField(max_length=500, blank=True)
    benefit_4= models.CharField(max_length=200, blank=True)
    benefit_4_disc= models.CharField(max_length=500, blank=True)  
    #Section 2:
    section_2_h2= models.CharField(max_length=200, blank=True)
    service_1= models.CharField(max_length=200, blank=True)
    service_1_disc= models.CharField(max_length=500, blank=True)
    service_2= models.CharField(max_length=200, blank=True)
    service_2_disc= models.CharField(max_length=500, blank=True)
    service_3= models.CharField(max_length=200, blank=True)
    service_3_disc= models.CharField(max_length=500, blank=True)
    service_4= models.CharField(max_length=200, blank=True)
    service_4_disc= models.CharField(max_length=500, blank=True)  
    service_5= models.CharField(max_length=200, blank=True)
    service_5_disc= models.CharField(max_length=500, blank=True)  
    service_6= models.CharField(max_length=200, blank=True)
    service_6_disc= models.CharField(max_length=500, blank=True)  
    #section 3:
    section_3_h2= models.CharField(max_length=200, blank=True)
    section_3_content= models.CharField(max_length=500, blank=True)
    def __str__(self):
        return self.service_name

    
    