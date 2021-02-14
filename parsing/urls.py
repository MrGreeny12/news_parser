from django.urls import path
from .views import PostsView


app_name = 'parsing'

urlpatterns = [
    path('posts', PostsView.as_view()),
]