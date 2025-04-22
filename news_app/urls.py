from django.urls import path
from . import views
from .views import like_article
from .views import submit_article
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("articles/<int:id>/", views.article_detail, name="article_detail"),
    path('search/', views.search_articles, name='search_articles'),
    path('like/<int:article_id>/', like_article, name='like_article'),
    path("articles/<int:article_id>/comment/", views.add_comment, name="add_comment"),
    path("submit/", submit_article, name="submit_article"),
    path('api/articles/', views.articles_api, name='articles_api'),
    path('delete_article/<int:id>/', views.delete_article, name='delete_article'),
    path('api/article/<int:id>/', views.articles_api, name='article_detail_api'),
    path("submit_advertisement/", views.submit_advertisement, name="submit_advertisement"),
    path("edit_article/<int:id>/", views.edit_article, name="edit_article"),
]

if settings.DEBUG:
    urlpatterns += static(settings.DATA_URL, document_root=settings.DATA_ROOT)
