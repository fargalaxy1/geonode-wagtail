from django.conf import settings
from django import template

from geonode.contrib.wagtail_.models import BlogPage

register = template.Library()

# Blog feed for home page
@register.inclusion_tag(
    'wagtail_/tags/blog_posts_homepage.html',
    takes_context=True
)
def blog_posts_homepage(context, count=2):
    blogs = BlogPage.objects.all()
    return {
        'blogs': blogs,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }
