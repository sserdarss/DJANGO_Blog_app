
from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm



class UserForm(UserCreationForm):
    class Meta():
        model = User
        # fields = '__all__'
        fields = ('username', 'password1', 'password2', 'bio', 'profile_pic')
        # exclude = ('is_staff', 'is_active', 'date_joined', 'password', 'last_login', 'is_superuser', 'groups', 'user_permissions', )


class RegisterForm(UserCreationForm):
    class Meta():
        model = User

        fields = ('username','email', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    class Meta():
        model = User

        fields = ('username','email','profile_pic','bio')
        