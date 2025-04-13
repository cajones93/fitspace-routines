from django.views.generic import ListView
from blog.models import Post


class Index(ListView):
    template_name = 'home/index.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return self.model.objects.all()[:3]