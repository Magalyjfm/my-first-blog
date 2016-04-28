from django.db import models

from django.utils import timezone


class Post(models.Model):
	author = models.ForeignKey('auth.user')
	titulo = models.CharField(max_length=200)
	texto = models.TextField()
	fecha_crea = models.DateTimeField(default=timezone.now)
	fecha_publi = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()


	def __str__(self):
		return self.titulo
		pass

