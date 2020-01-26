from django.shortcuts import render
from django.urls import reverse_lazy


# Create your views here.

from django.http import HttpResponse

from django.views.generic import View, ListView, DetailView, UpdateView, DeleteView
from .models import Post

class PostView(View):
    
    def get(self,request):
        post = Post.objects.get(pk=3)
        print(post.get_absolute_url())

        return HttpResponse(post)

class PostListView(ListView):
    # queryset = Post.objects.all()
    model = Post

    # def get_queryset(self):
    #     return Post.objects.filter(pk=1)
    

class PostDetailView(DetailView):

    # queryset = Post.objects.all()
    model = Post

    context_object_name = "post"

class PostUpdateView(UpdateView):
    model = Post
    fields = '__all__'


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("post_list")