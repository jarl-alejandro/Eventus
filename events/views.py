from django.shortcuts import render
from django.views.generic import TemplateView

from mixins import LoginRequired

class InicioView(TemplateView):
	template_name = "inicio.html"

class AppView(LoginRequired, TemplateView):
	template_name = "app.html"