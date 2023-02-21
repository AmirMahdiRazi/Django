from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get("cat_name") != None:
        posts = Post.objects.filter(category__name=kwargs["cat_name"])
    if kwargs.get("author_username") != None:
        posts = Post.objects.filter(author__username=kwargs["author_username"])

    posts = Paginator(posts, 3)

    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    context = {'posts': posts}
    return render(request, 'blogs/blog-home.html', context)


def blog_single(request, pid):
    # Way 2
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid, status=1)
    # post = Post.objects.filter(status=1, id=1)
    instance = Post.objects.values_list('id', 'title')
    posts_list = list(instance)
    index = posts_list.index((post.id, post.title))
    prev_post = None
    next_post = None
    if (index == len(posts_list) - 1):
        prev_post = posts[index-1]
    elif (index == 0):
        next_post = posts[index+1]
    else:
        next_post = posts[index+1]
        prev_post = posts[index-1]
    context = {'post': post, 'next_post': next_post, 'prev_post': prev_post}
    return render(request, 'blogs/blog-single.html', context)


def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = Post.objects.filter(category__name=cat_name)
    context = {'posts': posts}
    return render(request, 'blogs/blog-home.html', context)


def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if (s := request.GET.get('s')):
            posts = Post.objects.filter(content__contains=s)

    context = {'posts': posts}
    return render(request, 'blogs/blog-home.html', context)


def blog_temp(requset):
    return render(requset, 'temp.html')
