from django.urls import path
from .views import AddPost, Posts


urlpatterns = [
    path('', AddPost.as_view(), name='add_post'),
    path('posts/', Posts.as_view(), name='posts'),
]