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
    job_description = models.TextField()
    location = models.CharField(max_length=100)
    last_date_to_apply = models.DateField()
    domain = models.CharField(max_length=200, null=False)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('job_detail', args=[str(self.id)])


