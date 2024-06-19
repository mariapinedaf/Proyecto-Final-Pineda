from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('create/', views.create_post, name='create_post'),
    path('detail/<int:id>/', views.detail_post, name='detail_post'),
    path('delete/<int:id>/', views.delete_post, name='delete_post'),
    path('posts/', views.list_posts, name='list_posts'),
]