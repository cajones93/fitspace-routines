from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'title',
        'slug',
        'focus',
        'status',
        'created_on',
    )
    search_fields = ['title', 'content', 'focus']
    list_filter = ('status', 'focus')
    prepopulated_fields = {'slug': ('title',)}
