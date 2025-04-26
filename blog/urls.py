from django.urls import path
from .views import (
    AddPost, Posts, 
    PostDetail, DeletePost, 
    UpdatePost
)


urlpatterns = [
    path("", AddPost.as_view(), name="add_post"),
    path("posts/", Posts.as_view(), name="posts"),
    path("<slug:slug>/", PostDetail.as_view(), name="post_detail"),
    path("delete/<slug:slug>/", DeletePost.as_view(), name="delete_post"),
    path("edit/<slug:slug>/", UpdatePost.as_view(), name="update_post"),
    # path('<slug:slug>/edit_comment/<int:comment_id>',
    #      views.comment_edit, name='comment_edit'),
    # path('<slug:slug>/delete_comment/<int:comment_id>',
    #      views.comment_delete, name='comment_delete'),
]
