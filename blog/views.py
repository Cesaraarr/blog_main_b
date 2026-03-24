from django.shortcuts import render

# Create your views here.
from django.db.models import Q
from django.shortcuts import render, get_list_or_404, render

from.models import Post, Category

# Create your views here.
def home(request):
    posts = Post.objects.filter(status=Post.ACTIVATE).order_by('-created_at')
    context = {

        'post': posts
    }
    return render(request, 'blog/home.html', context)
