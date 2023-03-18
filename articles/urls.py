from django.urls import path
from .views import ArticlesView, CreateArticle, UpdateArticle, DeleteArticle, ArticleDetails


urlpatterns = [
    path('', ArticlesView.as_view(), name='article_list'),
    path('add/', CreateArticle.as_view(), name='add_article'),
    path('<int:pk>', ArticleDetails.as_view(), name='article_detail'),
    path('<int:pk>/update', UpdateArticle.as_view(), name='update_article'),
    path('<int:pk>/delete', DeleteArticle.as_view(), name='delete_article'),
]