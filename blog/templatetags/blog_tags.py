from django import template
from blog.models import Post
from blog.models import Category

register = template.Library()


@register.simple_tag(name='totalposts')
def funtion():
    posts = Post.objects.filter(status=1).count()
    return posts


@register.simple_tag(name='posts')
def funtion():
    posts = Post.objects.filter(status=1)
    return posts


@register.filter
def snippet(value, arg=20):
    return value[:arg] + "..."


@register.inclusion_tag('blogs/blog-popular-posts.html')
def latestposts(arg=3):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts': posts}


@register.inclusion_tag('blogs/blog-post-categories.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    dict_cat = {}
    for name in categories:
        dict_cat[name] = posts.filter(category=name).count()
    return {'dict_cat': dict_cat}
