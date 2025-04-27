from django.urls import path
from .views import (
    AddPost, Posts, 
    PostDetail, DeletePost,
    UpdatePost, CreateComment,
    EditComment, DeleteComment
)


urlpatterns = [
    path("", AddPost.as_view(), name="add_post"),
    path("posts/", Posts.as_view(), name="posts"),
    path("<slug:slug>/", PostDetail.as_view(), name="post_detail"),
    path("delete/<slug:slug>/", DeletePost.as_view(), name="delete_post"),
    path("edit/<slug:slug>/", UpdatePost.as_view(), name="update_post"),
    path('post/<slug:slug>/comment/', CreateComment.as_view(), name='add_comment'),
    path('comment/edit/<int:comment_id>/', EditComment.as_view(), name='edit_comment'),
    path('comment/delete/<int:comment_id>/', DeleteComment.as_view(), name='delete_comment'),
]
