from django.urls import path
from .views import  post_create,show_post, post_detail, like



urlpatterns = [
    path('post_create/',post_create,name='post_create'),
    path("post_list/",show_post, name="post_list"),
    path("<str:slug>/",post_detail, name="detail"),
    path("<str:slug>/like/",like, name="like"),
]