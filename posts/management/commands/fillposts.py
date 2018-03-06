from django.core.management.base import BaseCommand

from posts.models import Post

from themes.models import Themes


TEST_TITLE = 'Test post # %s'

SUCCESS_TEXT = 'Post %s created successfully.'

LOREM_DESCRIPTION = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque tempor sit amet enim scelerisque interdum. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. In eu finibus erat.'

LOREM_BODY = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque tempor sit amet enim scelerisque interdum. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. In eu finibus erat. Vivamus varius dolor nec pellentesque faucibus. Ut sed lacinia felis. Vestibulum sit amet tincidunt lorem. In eu sem dictum, lobortis nisi ac, dictum mauris. Sed quis erat sem. Sed lobortis fermentum turpis accumsan interdum. Aenean posuere commodo massa, ac sodales lorem venenatis sit amet. Ut interdum nibh sapien, a consequat massa accumsan at. Vestibulum ut suscipit mauris. Morbi ut erat orci.

Fusce rutrum nibh eget blandit facilisis. Nunc maximus venenatis purus imperdiet fermentum. Nam ut libero sed tortor lobortis fermentum. Etiam rutrum ullamcorper odio at ultricies. In at libero mollis, venenatis nibh vel, viverra ante. Vivamus suscipit leo eget tortor tincidunt vehicula. Donec porttitor semper sagittis. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac felis id ante ultricies interdum bibendum a metus. Aliquam semper eget risus id tristique. Sed egestas mauris ut ligula ullamcorper, nec semper mauris pharetra. Integer at enim non purus congue molestie. Donec ac ligula nec augue dignissim porta vulputate sed orci. Morbi tincidunt faucibus lectus, ut lacinia diam varius et. Praesent at gravida dui.
'''


class Command(BaseCommand):

    help = 'Generate Post instances'


    def add_arguments(self, parser):

        parser.add_argument('num', type=int)

        parser.add_argument('--theme', required=False, type=int)


    def handle(self, *args, **options):

        theme = None

        num = options['num']

        theme_id = options['theme']

        last_instance = Post.objects.last()

        start_num = last_instance.id  if last_instance else 1

        end_num = start_num + int(num)

        if theme_id:

            theme = Themes.objects.get(id=theme_id)

        for idx in range(start_num, end_num):

            post = Post()

            post.title = TEST_TITLE % idx

            post.description = LOREM_DESCRIPTION

            post.posttext = LOREM_BODY

            if theme:

                post.theme = theme

            post.save()

            self.stdout.write(self.style.SUCCESS(SUCCESS_TEXT % idx))
