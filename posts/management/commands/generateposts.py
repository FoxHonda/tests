from django.core.management.base import BaseCommand, CommandError

from posts.models import Post

from themes.models import Themes

class Command(BaseCommand):
	
	help = 'Generate Post instances'

	def add_arguments(self, parser):
		parser.add_argument('num', type=int)
		parser.add_argument('theme', type=int)

	def handle(self, *args, **options):
		
		num  = options['num']
		theme_id = options['theme']
		
		if theme_id:
			theme = Themes.objects.get(id=theme_id)
		
		for idx in range(num):
			post = Post()
			post.title = 'Post # %s' % idx
			post.description = 'Post # %s description' % idx
			post.body = 'Post # %s body' % idx
			if theme:
				post.theme = theme

			post.save()



		#print(options)
		#if 'theme' in options:
		#	print(options['theme'])
		