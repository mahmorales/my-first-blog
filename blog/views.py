from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})

from django.shortcuts import render
from .models import Post

from django.utils import timezone

from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
