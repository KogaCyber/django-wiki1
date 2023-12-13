from django.urls import path
from .views import *

urlpatterns = [
    path('', index_html, name='index'),
    path('article/<int:pk>/', article, name='article'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('article/<int:pk>/update/', EditArticle.as_view(), name='update'),
    path('random_page/', RandomPage.as_view(), name='random_page'),
    path('search/', search, name='search'),
    path('add_article/', AddArticle.as_view(), name='add_article'),
]
