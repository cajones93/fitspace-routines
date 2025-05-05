from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "author",
        "title",
        "slug",
        "focus",
        "status",
        "created_on",
    )
    search_fields = ["title", "content", "focus"]
    list_filter = ("status", "focus")
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = 'content'
    actions = ['publish_posts']

    def publish_posts(self, request, queryset):
        """
        Action to bulk publish posts in the admin page.
        """
        queryset.update(status=1)


admin.site.register(Comment)
