from django.urls import path
from . import views
from .views import user_center



urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('authors/', views.author_list, name='author_list'),
    path('authors/<int:author_id>/', views.author_posts, name='author_posts'),
    path('date/<int:year>/<int:month>/<int:day>/', views.date_posts, name='date_posts'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('new/', views.new_post, name='new_post'),
    path('search/', views.search, name='search'),
    path('author/<str:username>/', views.author_posts, name='author_posts'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/delete/', views.post_delete, name='post_delete'),
    path('user_center/', user_center, name='user_center'),
]