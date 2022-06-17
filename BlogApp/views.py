from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from .models import *

class HomeView(ListView):
    model = Post
    template_name = 'BlogApp/home.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'BlogApp/post.html'
    context_object_name = 'post'