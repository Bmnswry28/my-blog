from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Post, Category

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['index', 'category_list', 'about', 'post_titles']

    def location(self, item):
        return reverse(item)

class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Post.objects.filter(status='published')

    def lastmod(self, obj):
        return obj.updated_at

class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Category.objects.filter(slug__isnull=False).exclude(slug='')

    def location(self, obj):
        if obj.slug:
            return reverse('category_detail', args=[obj.slug])
        return ''

sitemaps = {
    'static': StaticViewSitemap,
    'posts': PostSitemap,
    'categories': CategorySitemap,
}