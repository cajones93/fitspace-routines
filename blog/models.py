from django.db import models
from django.contrib.auth.models import User

from djrichtextfield.models import RichTextField


FOCUS = (
    ("general_fitness", "General Fitness"),
    ("strength", "Strength"),
    ("hypertrophy", "Hypertrophy"),
    ("weight_loss", "Weight Loss"),
)
STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    A model to create and mange a blog post entry related to :model:`auth.User`.
    """

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_author"
    )
    title = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    focus = models.CharField(choices=FOCUS, default="general-fitness")
    excerpt = models.CharField(max_length=500, null=False, blank=False)
    content = RichTextField(max_length=10000, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on", "author", "focus"]

    def __str__(self):
        return f"{self.title} | A {self.focus} program shared by {self.author}"


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`blog.Post`
    and :model:`auth.User`.
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField(default="")
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["created_on", "author"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
