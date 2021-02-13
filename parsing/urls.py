from django.urls import path
from .views import PostView


app_name = 'parsing'

urlpatterns = [
    path('posts', PostView.as_view()),
]