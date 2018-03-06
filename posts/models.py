from django.db import models

class Post(models.Model):

	title = models.CharField(max_length=150)
	image = models.ImageField(null=True, blank=True)
	description = models.TextField()
	posttext = models.TextField()
	theme = models.ForeignKey('themes.Themes', null=True, blank=True, on_delete=models.SET_NULL)
	
	def __str__(self):
		return self.title