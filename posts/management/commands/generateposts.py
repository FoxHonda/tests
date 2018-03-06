from django.core.management.base import BaseCommand, CommandError

from posts.models import Post

from themes.models import Themes


BODY_TEXT = """
Lorem ipsum dolor sit amet, consectetur adipisicing elit. 
Voluptas soluta ab distinctio molestias quasi repellendus 
necessitatibus sunt nesciunt aut nihil asperiores vero officiis 
praesentium numquam architecto animi perspiciatis hic, assumenda 
velit. Fugiat, debitis voluptatum impedit, excepturi illum recusandae. 
Quibusdam dolore a beatae assumenda voluptatem quasi qui et! Animi quam 
voluptatum omnis, maxime officiis ratione facere explicabo! Tempore, odit, 
consectetur. Porro iste repellendus exercitationem facere molestias? 
Quod assumenda aliquid sint veritatis dolorem dolore provident, 
sapiente ut voluptates, architecto voluptate ratione nemo iure officia 
laboriosam est, id fuga neque cum corporis eligendi! Deleniti ipsam culpa soluta, 
itaque doloribus tempore, necessitatibus minus repellat, molestias distinctio 
hic excepturi possimus dolor. Fuga voluptates eaque sapiente molestias illum 
minima, labore unde molestiae. Voluptatem officiis nisi doloribus architecto beatae, 
repellendus culpa voluptate ex hic laboriosam eius dolore alias! Ratione autem 
earum adipisci sunt ex, odit suscipit cum aspernatur, eveniet eius iure 
perspiciatis placeat, maiores mollitia quia quam rem magnam corporis sint. 
Ad voluptatem maiores iusto et, vero cum asperiores odio molestias earum 
quo aperiam! Nisi ipsum numquam cumque illum veritatis. Inventore perferendis 
architecto voluptas mollitia illo, dolorum saepe. Perspiciatis ex non eaque 
numquam enim repellat et, at corporis illo aspernatur quod distinctio, deleniti! 
Magni at atque, enim, ducimus tempore cupiditate id quisquam tenetur. 
Vitae nemo consectetur numquam excepturi sint necessitatibus, obcaecati 
libero eius reiciendis magnam vel eligendi doloremque commodi voluptatem 
ipsam quaerat at sit sunt assumenda architecto eaque sapiente! Debitis deserunt 
cumque inventore sapiente veniam, vel libero odio, corporis, consectetur 
asperiores tenetur molestias. Tempora placeat obcaecati unde, dicta, 
non laboriosam. Itaque repellat sequi laborum dolore cupiditate deserunt tempore, 
blanditiis ex aliquam aliquid cum asperiores? Nostrum suscipit eligendi 
possimus molestias velit ipsa, facere, assumenda illo odio quisquam modi 
maiores veritatis recusandae deserunt excepturi debitis dolores soluta 
laudantium dolorem blanditiis eos voluptates! Voluptas esse cupiditate 
consectetur quidem quae corporis.
"""
DESC_TEXT = 'Itaque repellat sequi laborum dolore cupiditate deserunt tempore.'
POST_TITLE = 'Test Post #'

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
			post.title = '%s # %s' % (POST_TITLE, idx)
			post.description = DESC_TEXT
			post.posttext = BODY_TEXT
			if theme:
				post.theme = theme

			post.save()



		#print(options)
		#if 'theme' in options:
		#	print(options['theme'])
		