from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
	class Meta:
		model = Evento
		fields = ('titulo', 'descripcion', 'fecha', 'foto', 'lugar')

		widgets = {
			'fecha': forms.DateTimeInput(attrs = {
				'class' : "EvntoDateTime",
				#'type': "datetime-local"
			})
		}