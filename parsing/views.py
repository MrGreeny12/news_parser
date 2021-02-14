from rest_framework import generics
from rest_framework.response import Response
from .models import Post
from .serializers import PostsSerializer


class PostsView(generics.GenericAPIView):
    '''
    View for models db Posts with URL-params (order, offset, limit)
    '''
    def get(self, request):
        order = request.GET.getlist('order')
        offset = request.GET.getlist('offset')
        limit = request.GET.getlist('limit')
        if bool(limit):
            articles = Post.objects.all().order_by(*order)[:int(limit[0])]
        elif bool(offset):
            articles = Post.objects.all().order_by(*order)[int(offset[0]):5]
        elif bool(limit) and bool(offset):
            articles = Post.objects.all().order_by(*order)[int(offset[0]):int(limit[0])]
        else:
            articles = Post.objects.all().order_by(*order)[:5]
        serializer = PostsSerializer(articles, many=True)
        return Response({"posts": serializer.data})