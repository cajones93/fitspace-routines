from django.views.generic import (
    CreateView, ListView, 
    DetailView, DeleteView,
    UpdateView
)
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Q

from .models import Post
from .forms import BlogPostForm


class Posts(ListView):
    """View all posts"""

    template_name = "blog/posts.html"
    model = Post
    context_object_name = "posts"

    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        if query:
            posts = self.model.objects.filter(
                Q(title__icontains=query)|
                Q(focus__icontains=query)|
                Q(content__icontains=query)
            )
        else:
            posts = self.model.objects.all()
        return posts


class PostDetail(DetailView):
    """View a single post"""

    template_name = "blog/post_detail.html"
    model = Post
    context_object_name = "post"


class AddPost(LoginRequiredMixin, CreateView):
    """Add post view"""

    template_name = "blog/add_post.html"
    model = Post
    form_class = BlogPostForm
    success_url = "/posts/posts/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddPost, self).form_valid(form)


class DeletePost(LoginRequiredMixin, DeleteView):
    """ Delete a post """

    model = Post
    success_url = "/posts/posts/"


class UpdatePost(LoginRequiredMixin, UpdateView):
    """ Edit a post """
    template_name = "blog/edit_post.html"
    model = Post
    form_class = BlogPostForm
    success_url = "/posts/posts/"
