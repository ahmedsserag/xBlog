from django.contrib import admin
from .models import Post

admin.site.site_header = 'xBlog Admin Panel'
admin.site.site_title = 'xBlog'

# Posts Model
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'status', 'author', 'publish']
    search_fields = ['title', 'slug']
    ordering = ['author', 'status', 'publish']
    prepopulated_fields = {"slug": ["title"]}