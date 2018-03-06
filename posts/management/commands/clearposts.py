from django.core.management.base import BaseCommand

from posts.models import Post

from themes.models import Themes


SUCCESS_TEXT = 'Posts %s removed successfully.'

TEST_TITLE = 'Test Post #'


class Command(BaseCommand):

    help = 'Remove test post instances'


    def add_arguments(self, parser):

        parser.add_argument('--num', required=False, type=int)

        parser.add_argument('--theme', required=False, type=int)


    def handle(self, *args, **options):

        try:

            num = options['num']

            theme_id = options['theme']

            if theme_id:

                theme = Themes.objects.get(id=theme_id)

                posts_manager = theme.post_set

             #   self.stdout.write(theme_id)
            else:

                posts_manager = Post.objects

            posts = posts_manager.filter(title__startswith=TEST_TITLE)[:num]

            for post in posts:

                self.stdout.write(self.style.SUCCESS(SUCCESS_TEXT % post.id))

                post.delete()

        except Exception as e:

            self.stdout.write(self.style.ERROR(e))


