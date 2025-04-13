from django.urls import path
from .views import AddPost, Posts, PostDetail


urlpatterns = [
    path("", AddPost.as_view(), name="add_post"),
    path("posts/", Posts.as_view(), name="posts"),
    path("<slug:pk>/", PostDetail.as_view(), name="post_detail"),
]
