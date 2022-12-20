from django.contrib.sitemaps import Sitemap
from .models import Post


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.publish_date
        
    def location(self,obj):
        return '/post/%s' % (obj.title)