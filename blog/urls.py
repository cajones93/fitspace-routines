from django.urls import path
from .views import AddPost, Posts, PostDetail, DeletePost


urlpatterns = [
    path("", AddPost.as_view(), name="add_post"),
    path("posts/", Posts.as_view(), name="posts"),
    path("<slug:pk>/", PostDetail.as_view(), name="post_detail"),
    path("delete/<slug:pk>/", DeletePost.as_view(), name="delete_post"),
]
