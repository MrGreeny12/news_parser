from django.core.management.base import BaseCommand
from urllib.request import urlopen
from bs4 import BeautifulSoup
from parsing.models import Articles


class Command(BaseCommand):
    help = 'collect articles'

    def handle(self, *args, **options):
        # сбор html
        html = urlopen('https://news.ycombinator.com/newest')
        soup = BeautifulSoup(html, 'html.parser')
        posts = soup.find_all('a', class_='storylink')

        for post in posts:
            # проверка кол-ва статей
            if len(posts) < 31:
                title = post.get_text(),
                url = post.get('href')
                try:
                    #сохранение в БД
                    Articles.objects.create(
                        title=title,
                        url=url,
                    )
                    print(f'{title} added')
                except:
                    print(f'{title} already exists')
            else:
                break

        self.stdout.write('Complete')