from django.db import models
NAME_HELP = 'Поле для хранения названия темы.'

class Themes(models.Model):

	name = models.CharField(verbose_name='Название',max_length=150, help_text=NAME_HELP)
	description = models.TextField(verbose_name='Описание',null=True, blank=True)		

	def __str__(self):
		return self.name