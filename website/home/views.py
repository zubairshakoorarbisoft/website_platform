from django.conf import settings
from django.views.generic import TemplateView

from clients.models import Testimonial


class HomePageView(TemplateView):
    template_name = "home/home_light.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the testimonials and pass them to the context
        testimonials = Testimonial.objects.all()
        context["testimonials"] = testimonials
        context["MEDIA_URL"] = settings.MEDIA_URL

        return context
