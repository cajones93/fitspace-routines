from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Post

class BlogPostForm(forms.ModelForm):
    """ Form to create a post """
    class Meta:
        model = Post
        fields = ['title', 'focus', 'excerpt', 'content']
        
        content = forms.CharField(widget=RichTextWidget())

        labels = {
            'title': 'Program Name',
            'focus': 'Workout Focus',
            'excerpt': 'Brief Description',
            'content': 'Program Details'
        }