from django.views.generic import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post
from .forms import BlogPostForm


class AddPost(LoginRequiredMixin, CreateView, ):
    """ Add post view """
    template_name = 'blog/add_post.html'
    model = Post
    form_class = BlogPostForm
    success_url = '/index/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddPost, self).form_valid(form)
