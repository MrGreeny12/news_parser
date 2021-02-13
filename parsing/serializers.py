from django.utils import timezone
from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    '''
    Serializer for model db Post
    '''
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=250)
    url = serializers.CharField(max_length=250)
    created_date = serializers.DateTimeField(default=timezone.now)