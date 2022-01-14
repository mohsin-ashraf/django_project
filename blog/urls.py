from django.urls import path
from .views import (
    PostListView, 
    DetailPostView, 
    CreatePostView,
    UpdatePostView,
    DeletePostView,
    PostUserListView
)

from . import views

urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('post/<int:pk>/', DetailPostView.as_view(), name='post-detail'),
    path('post/new/', CreatePostView.as_view(), name='post-create'),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='post-delete'),
    path('post/<int:pk>/update/', UpdatePostView.as_view(), name='post-update'),
    path('user/<str:username>', PostUserListView.as_view(), name='user-posts'),
    path('about/', views.about, name="blog-about")
]
