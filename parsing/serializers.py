from django.utils import timezone
from rest_framework import serializers


class PostsSerializer(serializers.Serializer):
    '''
    Serializer for model db Post
    '''
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=250)
    url = serializers.CharField(max_length=250)
    created = serializers.DateTimeField(default=timezone.now)