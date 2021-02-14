from django.core.management.base import BaseCommand
from urllib.request import urlopen
from bs4 import BeautifulSoup
from parsing.models import Post


class Parse(BaseCommand):
    help = 'collect articles'

    def handle(self, *args, **options):
        # collecting html data
        html = urlopen('https://news.ycombinator.com/news')
        soup = BeautifulSoup(html, 'html.parser')
        posts = soup.find_all('a', class_='storylink')
        for post in posts:
            # checking count of posts
            if len(posts) < 31:
                title = post.get_text(),
                url = post.get('href')
                try:
                    # save in db
                    Post.objects.create(
                        title=title,
                        url=url,
                    )
                    print(f'{title} added')
                except:
                    print(f'{title} already exists')
            else:
                break

        self.stdout.write('Complete')