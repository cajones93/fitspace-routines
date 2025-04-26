from django.urls import path
from .views import (
    AddPost, Posts, 
    PostDetail, DeletePost,
    UpdatePost, CreateComment
)


urlpatterns = [
    path("", AddPost.as_view(), name="add_post"),
    path("posts/", Posts.as_view(), name="posts"),
    path("<slug:slug>/", PostDetail.as_view(), name="post_detail"),
    path("delete/<slug:slug>/", DeletePost.as_view(), name="delete_post"),
    path("edit/<slug:slug>/", UpdatePost.as_view(), name="update_post"),
    path('post/<slug:slug>/comment/', CreateComment.as_view(), name='add_comment'),
]
