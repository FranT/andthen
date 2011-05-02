from django.db import models

class Historia(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	is_open=models.BooleanField()

class Fragmento(models.Model):
	contenido=models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	historia = models.ForeignKey(Historia)

# Create your models here.


