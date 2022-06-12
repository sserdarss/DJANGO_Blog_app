from django.shortcuts import render, redirect, get_object_or_404
from blog.forms import  PostForm, CommentForm
from .models import  Post, Like , PostView 



def post_create(request):
    post_form = PostForm()

    if request.method == "POST" :
        post_form = PostForm(request.POST, request.FILES)  
         
        if post_form.is_valid():
            post_form.instance.user = request.user
            post_form.save()
            return redirect("home")
            
    context = {
        "post_form": post_form,
    }

    return render(request, 'blog/post_create.html', context)

def show_post(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }

    return render(request, 'blog/post_list.html', context)






def post_detail(request, slug):
    # comment = Comment.objects.all( )
    # kim = request.user
    form = CommentForm()
    obj = get_object_or_404(Post, slug=slug)
    # like_qs = Like.objects.filter(user=request.user, post=obj)
    if request.user.is_authenticated:
        PostView.objects.get_or_create(user=request.user, post=obj)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = obj
            comment.save()
            return redirect("detail", slug=slug)
            # return redirect(request.path)
    context = {
        'object' : obj,
        "form" : form,
        
    }
    return render(request, "blog/post_detail.html", context)



def like(request, slug):
    if request.method == "POST":
        obj = get_object_or_404(Post, slug=slug)
        like_qs = Like.objects.filter(user=request.user, post=obj)
        
        if like_qs.exists():
            like_qs[0].delete()
        else:
            Like.objects.create(user=request.user, post=obj)
        return redirect("detail", slug=slug)
    return redirect("detail", slug=slug)

