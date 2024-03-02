from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator

class Job(models.Model):
    display_title = models.CharField(max_length=100)
    no_of_positions = models.IntegerField(
        validators=[MinValueValidator(1)]
    )
    is_remote = models.BooleanField()
    is_on_site = models.BooleanField()
    company_name = models.CharField(max_length=200, default="")
    company_disc = models.CharField(max_length=500, blank=True)
    location = models.CharField(max_length=100)
    last_date_to_apply = models.DateField()
    domain = models.CharField(max_length=200, null=False)
    active = models.BooleanField(default=True)
    salary = models.CharField(default="", max_length=10)
    SALARY_TYPE = {
        "Per Month":"P/ Month",
        "Per Hour":"P/ Hour",
        "Per Year":"P/ Year",
     }   
    salary_type = models.CharField(choices=SALARY_TYPE, default="", max_length=20)    
    job_description = models.TextField()
    job_requirement = models.TextField( blank=True)
    job_qualifications = models.TextField( blank=True)
    job_skills = models.TextField( blank=True)



    def get_absolute_url(self):
        return reverse('job_detail', args=[str(self.pk)])


