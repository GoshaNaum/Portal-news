from django.urls import reverse_lazy
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Author
from .filters import PostFilter
from .forms import PostForm

class PostsList(ListView):
    model = Post
    post_title = 'title'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 4


    def get_queryset(self):

       queryset = super().get_queryset()

       self.filterset = PostFilter(self.request.GET, queryset)

       return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['filterset'] = self.filterset
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

class PostSearch(ListView):
    model = Post
    ordering = '-posting_time'
    template_name = 'post_search.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class PostCreate(CreateView, PermissionRequiredMixin):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    permission_required = 'add_news'
    success_url = reverse_lazy('news_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.choice_field = 'news'
        post.author = Author.objects.get(user=self.request.user)
        return super().form_valid(form)


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    success_url = reverse_lazy('post_list')


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')

class ArticlesPost(ListView):
    model = Post
    template_name = 'articles.html'
    context_object_name = 'articles'

class NewsPost(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'


class NewsCreate(CreateView, PermissionRequiredMixin):
    form_class = PostForm
    model = Post
    permission_required = 'add_news'
    template_name = 'post_edit.html'
    success_url = reverse_lazy('news_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.choice_field = 'news'
        post.author = Author.objects.get(user=self.request.user)
        return super().form_valid(form)

class ArticleCreate(CreateView, PermissionRequiredMixin):
    form_class = PostForm
    model = Post
    permission_required = 'add_news'
    template_name = 'post_edit.html'
    success_url = reverse_lazy('news_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.choice_field = 'article'
        post.author = Author.objects.get(user=self.request.user)
        return super().form_valid(form)



