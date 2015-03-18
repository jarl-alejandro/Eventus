from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, ListView, DetailView

from .mixins import LoginRequired
from .forms import EventoForm
from .models import Evento

class InicioView(TemplateView):
	template_name = "inicio.html"

class AppView(LoginRequired, ListView):
	template_name = "app.html"
	model = Evento
	context_object_name = "eventos"

class EventDetailView(LoginRequired, DetailView):
	model = Evento
	template_name = "evento_detail.html"
	slug_field = 'slug'
	context_object_name = 'evento' 

class CreateEventView(LoginRequired, CreateView):
	template_name =  "create_events.html"
	form_class = EventoForm
	model = Evento
	success_url = '/app/'

	def form_valid(self, form):
		form.instance.creador = self.request.user
		return super(CreateEventView, self).form_valid(form)