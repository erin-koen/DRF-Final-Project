from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


class IndexTemplateView(LoginRequiredMixin, TemplateView):
    # LRMixin means only authenticated users can interact with app, LRMixin
    # redirects them automatically. 

    def get_template_names(self):
        template_name = "index.html"
        return template_name