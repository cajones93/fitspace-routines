from django.views.generic import (
    CreateView, ListView,
    DetailView, DeleteView,
    UpdateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.utils.text import slugify

from .models import Post
from .forms import BlogPostForm


class Posts(ListView):
    """View all posts"""

    template_name = "blog/posts.html"
    model = Post
    context_object_name = "posts"
    paginate_by = 6  # You might want to add pagination

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset().order_by('-created_on')
        query = self.request.GET.get('q')
        focus_filter = self.request.GET.get('focus')

        if focus_filter and focus_filter != 'All':
            queryset = queryset.filter(focus=focus_filter)

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(focus__icontains=query) |
                Q(content__icontains=query)
            )
        return queryset


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
        form.instance.author = self.request.user
        title = form.cleaned_data['title'] 
        slug = slugify(title)

        # Check if the slug already exists and add a number to make sure it is unique
        original_slug = slug
        counter = 1
        while Post.objects.filter(slug=slug).exists():
            slug = f"{original_slug}-{counter}"
            counter += 1
        form.instance.slug = slug
        return super().form_valid(form)


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

