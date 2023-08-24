from django.contrib.sitemaps import Sitemap
from Blog.models import Post
from django.urls import reverse


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.publish_date

    def location(self,obj):
        return '/post/%s' % (obj.slug)

class StaticSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7
    protocol = 'https'

    def items(self):
        return ['home', 'about', 'recents']

    def location(self, item):
        return reverse(item)