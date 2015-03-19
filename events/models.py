from django.db import models
from django.template.defaultfilters import slugify
from users.models import User

class Evento(models.Model):
	titulo = models.CharField(max_length = 140)
	descripcion = models.TextField()
	creador = models.ForeignKey(User)
	fecha = models.DateTimeField()
	foto = models.ImageField(upload_to = "foto")
	slug = models.SlugField(editable = False)
	lugar = models.CharField(max_length = 140, default = "")

	def __unicode__(self):
		return "%s (%s)" % (self.titulo, self.creador.email)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.titulo)
		super(Evento, self).save(*args, **kwargs)

	def photo(self):
		return "<img src='%s' width='100' />" % self.foto.url

	photo.allow_tags = True

class Comentar(models.Model):
	evento = models.ForeignKey(Evento)
	user = models.ForeignKey(User)
	comentario = models.CharField(max_length = 140)

	def __unicode__(self):
		return self.comentario