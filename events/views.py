from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.generic import TemplateView, CreateView, ListView, DetailView

from .mixins import LoginRequired
from .forms import EventoForm
from .models import Evento, Comentar

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

	def get_context_data(self, **kwargs):
	    context = super(EventDetailView, self).get_context_data(**kwargs)
	    comentarios = Comentar.objects.filter(evento = context['object']).order_by('-id')
	    
	    data = {
	    	'comentarios':comentarios
	    }

	    context.update(data)
	    return context

class CreateEventView(LoginRequired, CreateView):
	template_name =  "create_events.html"
	form_class = EventoForm
	model = Evento
	success_url = '/app/'

	def form_valid(self, form):
		form.instance.creador = self.request.user
		return super(CreateEventView, self).form_valid(form)


def guardar_comentario(request):
	if request.is_ajax():
		if request.POST["comentarioEnviar"]:
			comentario = Comentar(comentario = request.POST["comentarioEnviar"],
				evento_id = request.POST["eventoId"], user = request.user)
			comentario.save()

		comentarios = Comentar.objects.filter(evento__id = request.POST["eventoId"]).order_by('-id')
		
		data = [{
			'avatar': comentario.user.avatar.url,
			'comentario':comentario.comentario,
			'email': comentario.user.email
		} for comentario in comentarios]
		
		return JsonResponse(data, safe=False)