from django.contrib.sitemaps import Sitemap
from blogApp.models import Post


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Post.objects.filter(status='Published')

    def lastmod(self, obj):
        return obj.updated