from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer


class PostView(APIView):
    '''
    View for models db Posts
    '''
    def get(self, request):
        articles = Post.objects.all()
        serializer = PostSerializer(articles, many=True)
        return Response({"posts": serializer.data})