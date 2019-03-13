from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Article

class PostForm(forms.ModelForm):

    class Meta:

        model = Article
        exclude = ('author', )
        # fields = ['title', 'image', 'description', 'related', 'content']

class RegisterForm(UserCreationForm):

    first_name = forms.CharField(max_length = 15, required = True)
    last_name = forms.CharField(max_length = 15, required = True)
    email = forms.EmailField()

    class Meta:

        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
