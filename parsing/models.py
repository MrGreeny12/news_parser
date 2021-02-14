from django.db import models
from django.utils import timezone


class Post(models.Model):
    '''
    Model post for db
    '''
    title = models.CharField(max_length=250)
    url = models.CharField(max_length=250, unique=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title