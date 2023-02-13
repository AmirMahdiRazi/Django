from django.shortcuts import render, get_object_or_404
from blog.models import Post
import asyncio


def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'blogs/blog-home.html', context)


def blog_single(request, pid):
    # Way 1
    # post = get_object_or_404(Post, pk=pid,status=1)
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
    print(index, prev_post, next_post)
    context = {'post': post, 'next_post': next_post, 'prev_post': prev_post}
    # context = {'post': post}
    return render(request, 'blogs/blog-single.html', context)
