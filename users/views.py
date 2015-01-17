from django.shortcuts import render
from django.views.generic import TemplateView

class UserHomepage(TemplateView):
    template_name = 'users.html'