from django.contrib import admin
from django.urls import path
import blog.views

urlpatterns = [
    path('', blog.views.home, name="home"),
    path('post/<int:post_id>', blog.views.detail, name = "detail"),
    path('post/new', blog.views.new, name="new"),
    path('post/<int:pk>/comment', blog.views.comment_new, name="comment_new"),
    path('post/<int:post_id>/edit', blog.views.edit, name='edit'),
    path('post/<int:post_id>/remove', blog.views.remove, name='remove'),
    path('comment/<int:comment_id>/remove', blog.views.comment_remove, name='comment_remove'),
]