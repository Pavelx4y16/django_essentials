from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}


class SecretView(LoginRequiredMixin, TemplateView):
    template_name = 'home/secret.html'
    login_url = '/admin'
