from django.urls import path
from .views import PostsList, PostDetail, PostCreate, PostUpdate, PostDelete, PostSearch, NewsCreate, ArticleCreate, ArticlesPost, NewsPost

urlpatterns = [
    path('', PostsList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('articles/create/', ArticleCreate.as_view(), name='articles_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('search/', PostSearch.as_view(), name='post_search'),
]