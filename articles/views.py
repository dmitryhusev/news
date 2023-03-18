from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Article
from django.urls import reverse_lazy

class ArticlesView(ListView):
    model = Article
    template_name = 'articles/articles.html'

class ArticleDetails(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'


class CreateArticle(CreateView):
    model = Article
    fields = ('title', 'body', 'author')
    template_name = 'articles/add_article.html'


class UpdateArticle(UpdateView):
    model = Article
    fields = ('title', 'body')
    template_name = 'articles/update_article.html'
    success_url = reverse_lazy('article_list')


class DeleteArticle(DeleteView):
    model = Article
    template_name = 'articles/delete_article.html'
    success_url = reverse_lazy('article_list')