from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta():
        model = Post

        fields = ('title','content','category','status')


class ShowForm(forms.ModelForm):
    class Meta():
        model = Post

        fields = ('title','user','content')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)







