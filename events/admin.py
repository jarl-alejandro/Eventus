from django.contrib import admin
from .models import Evento, Comentar

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
	list_display = ("titulo","creador", "photo")

@admin.register(Comentar)
class ComentarAdmin(admin.ModelAdmin):
	list_display = ("evento","user","comentario")