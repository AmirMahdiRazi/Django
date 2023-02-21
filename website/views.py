from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from blog.models import Post


def index_view(request):
    posts = Post.objects.filter(status=1).order_by("-published_date")[:6]
    context = {"posts": posts}
    return render(request, 'website\index.html', context)


def about_view(request):
    return render(request, 'website\\about.html')


def contact_view(request):
    return render(request, 'website\contact.html')


def elements_view(request):
    return render(request, 'website\elements.html')
