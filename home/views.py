from django.views.generic import ListView
from blog.models import Post


class Index(ListView):
    template_name = 'home/index.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        focus_filter = self.request.GET.get('focus')

        if focus_filter and focus_filter != 'All':
            queryset = queryset.filter(focus=focus_filter)

        return queryset[:3]
