from django.contrib import admin

from .models import Testimonial, Client, ClientQuery

# Register your models here.

admin.site.register(Testimonial)
admin.site.register(Client)
admin.site.register(ClientQuery)
