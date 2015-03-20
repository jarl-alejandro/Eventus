from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.generic import TemplateView

from .forms import UserCreationForm, EmailAuthenticationForm
from events.mixins import LoginRequired
from events.models import Evento

class ProfileView(LoginRequired, TemplateView):
	template_name = "profile.html"

	def get_context_data(self, **kwargs):
	    context = super(ProfileView, self).get_context_data(**kwargs)
	    eventos = Evento.objects.filter(creador = self.request.user)
	    data = { 'eventos':eventos }
	    context.update(data)
	    return context

def log_in(request):
	if request.method == "POST":
		form = EmailAuthenticationForm(request.POST)
		if form.is_valid():
			login(request, form.get_user())

		if request.user.is_authenticated():
			return redirect("/app/")
	else:
		form = EmailAuthenticationForm()
	return render(request, "login.html", { "form":form })

def registrate(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			email = request.POST["email"]
			password = request.POST["password1"]

			user = authenticate(email=email, password=password)

			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect("/app/")
				else:
					return HttpResponse("Usuario inactivo")
			else:
				return HttpResponse("Usuario incorrecto")
	else:
		form = UserCreationForm()
	return render(request, "registrate.html", { "form":form })


def log_out(request):
	logout(request)
	return redirect("/")