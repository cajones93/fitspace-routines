from django.urls import path
from .views import AddPost


urlpatterns = [
    path('', AddPost.as_view(), name='add_post'),
]