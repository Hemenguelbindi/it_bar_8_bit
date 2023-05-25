from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    post = Post.published.all()
    return render(request, 
                  'blog/post/list.html', 
                  {'posts': post})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, 
                             status=Post.Status.PUBLISHED, 
                             slug=post, 
                             publish__year=year, 
                             publish__month=month, 
                             publish__day=day,
                             )
    return render(request, 
                  'blog/post/list.html', 
                  {'posts': post})


