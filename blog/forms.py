from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post, Comment


class BlogPostForm(forms.ModelForm):
    """Form to create a post"""

    class Meta:
        model = Post
        fields = ["title", "focus", "excerpt", "content", "status"]

        widgets = {
            'content': SummernoteWidget(),
        }

        labels = {
            "title": "Program Name",
            "focus": "Workout Focus",
            "excerpt": "Brief Description",
            "content": "Program Details",
            "status": "Status"
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)
