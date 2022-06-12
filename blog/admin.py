from django.contrib import admin
from .models import Category, Post, Status, Comment, PostView, Like

admin.site.register(Post)
admin.site.register(Status)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(PostView)
admin.site.register(Like)