from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post
from .forms import BlogPostForm


class Posts(ListView):
    """View all posts"""

    template_name = "blog/posts.html"
    model = Post
    context_object_name = "posts"


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
    success_url = "/index/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddPost, self).form_valid(form)
