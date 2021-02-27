from django.shortcuts import render
from post.models import Post
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    obj = Post.objects.latest()
    recently = Post.objects.filter(created_date__lte=timezone.now()).reverse()[:3]
    last_four_post = Post.objects.filter(created_date__lte=timezone.now()).reverse()[:4]
    context = {
        'obj': obj,
        'recently': recently,
        'last_four_post': last_four_post,
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')
