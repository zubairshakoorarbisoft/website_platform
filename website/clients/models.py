from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

import os
from django.utils import timezone


def company_logo_upload_path(instance, filename):
    timestamp = timezone.now().strftime("%Y%m%d%H%M%S")
    filename, extension = os.path.splitext(filename)
    return f"{filename}_{timestamp}{extension}"


class Testimonial(models.Model):
    company_name = models.CharField(max_length=100, null=False)
    company_logo = models.FileField(upload_to=company_logo_upload_path, null=False)
    content = models.CharField(max_length=1000, null=False)
    giver_name = models.CharField(max_length=100, null=False)
    giver_designation = models.CharField(max_length=100, null=False)
    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )

#Skip thi model f0or now
class Client(models.Model):
    company_name = models.CharField(max_length=100, null=False)
    company_logo = models.FileField(null=False)
    website_url = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    address1 = models.CharField(max_length=100, null=True)
    address2 = models.CharField(max_length=100, null=True)
    phone_no = models.CharField(max_length=20, null=True)

#Skip thi model f0or now
class ClientQuery(models.Model):
    service_name = models.CharField(max_length=100, null=False)
    company_name = models.FileField(max_length=100, null=False)
    full_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    requirements = models.CharField(max_length=10000, null=True)
    active = models.BooleanField(default=True)


