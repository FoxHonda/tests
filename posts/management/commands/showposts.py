from django.core.management.base import BaseCommand

from posts.models import Post

from themes.models import Themes


TEST_TITLE = 'Test post #'


class Command(BaseCommand):

    help = 'Remove test post instances'


    def add_arguments(self, parser):

        parser.add_argument('--theme', required=False, type=int)


    def handle(self, *args, **options):

        try:

            theme_id = options['theme']

            if theme_id:

                theme = Themes.objects.get(id=theme_id)

                posts_manager = theme.post_set

            else:

                posts_manager = Post.objects

            posts = posts_manager.filter(title__startswith=TEST_TITLE)

            for post in posts:

                self.stdout.write(self.style.SUCCESS(post.title))

        except Exception as e:

            self.stdout.write(self.style.ERROR(e))


