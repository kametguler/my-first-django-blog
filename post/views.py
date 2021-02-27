from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, UpdateForm, CommentForm
from django.urls import reverse_lazy
# Create your views here.
'''
def posts(request):
    q = Post.objects.all()
    context = {
        'q': q
    }
    return render(request, 'list.html', context)
'''
class BlogsView(ListView):
    model = Post
    template_name = 'list.html'
    ordering = ['-created_date']
    #ordering = ['-id']


"""
class Create_View(CreateView):
    model = Post
    template_name = 'create_post.html'
    form_class = PostForm
    #fields = '__all__'

"""


class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('post')


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category__name=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.replace('-', ' '), 'category_posts': category_posts})


def DetailsView(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post.get_detail_url())
    else:
        form = CommentForm

    context={
        'post': post,
        'form': form,
    }
    return render(request, 'details.html', context)

def CreatePostView(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save()
        return redirect(post.get_absolute_url())
    context = {
        'form': form
    }
    
    return render(request, 'create_post.html', context)
