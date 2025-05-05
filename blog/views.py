from django.views.generic import (
    CreateView, ListView,
    DetailView, DeleteView,
    UpdateView
)
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.utils.text import slugify
from django.urls import reverse

from .models import Post, Comment
from .forms import BlogPostForm, CommentForm


class Posts(ListView):
    """View all posts"""

    template_name = "blog/posts.html"
    model = Post
    context_object_name = "posts"
    paginate_by = 6

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
                Q(content__icontains=query) |
                Q(author__username__icontains=query)
            )

        if self.request.user.is_authenticated:
            queryset = queryset.filter(
                Q(status=1) | Q(status=0, author=self.request.user)
            )
        else:
            queryset = queryset.filter(status=1)

        return queryset


class PostDetail(SuccessMessageMixin, DetailView):
    """View a single post and its comments"""
    template_name = "blog/post_detail.html"
    model = Post
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        comment_form = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = post.comments.all().order_by('created_on')
        comment_form['comments'] = comments
        comment_form['comment_form'] = CommentForm()

        return comment_form


class AddPost(LoginRequiredMixin, CreateView):
    """Add post view"""

    template_name = "blog/add_post.html"
    model = Post
    form_class = BlogPostForm

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
        messages.success(self.request, 'Post created successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('posts')


class DeletePost(LoginRequiredMixin, DeleteView):
    """ Delete a post """
    model = Post
    template_name = 'blog/post_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, 'Post deleted successfully.')
        return reverse('posts')


class UpdatePost(LoginRequiredMixin, UpdateView):
    """ Edit a post """
    template_name = "blog/edit_post.html"
    model = Post
    form_class = BlogPostForm

    def form_valid(self, form):
        messages.success(self.request, 'Post updated successfully.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'slug': self.object.slug})


class CreateComment(LoginRequiredMixin, CreateView):
    """ Create a new comment """
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, slug=self.kwargs['slug'])
        messages.success(self.request, 'Comment posted successfully and awaiting approval.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'slug': self.object.post.slug})


class EditComment(LoginRequiredMixin, UpdateView):
    """Edit a comment"""
    model = Comment
    form_class = CommentForm
    template_name = 'blog/edit_comment.html'
    pk_url_kwarg = 'comment_id'

    def form_valid(self, form):
        form.instance.approved = False
        messages.success(self.request, 'Comment updated successfully and awaiting approval.')
        return super().form_valid(form)

    def get_success_url(self):
        """Redirect to the post detail page after successful edit."""
        return reverse('post_detail', kwargs={'slug': self.object.post.slug})


class DeleteComment(LoginRequiredMixin, DeleteView):
    """Delete a comment"""
    model = Comment
    template_name = 'blog/delete_comment.html'
    pk_url_kwarg = 'comment_id'

    def get_success_url(self):
        """Redirect to the post detail page after successful deletion."""
        messages.success(self.request, 'Comment deleted successfully.')
        return reverse('post_detail', kwargs={'slug': self.object.post.slug})
