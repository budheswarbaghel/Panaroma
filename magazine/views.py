from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, DeleteView
from .models import Article
from .forms import RegisterForm, PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }

    return render(request, 'home.html', context)

def detail(request, article_id):

    article = get_object_or_404(Article, pk = article_id)
    context = {
        'article' : article,
    }
    
    return render(request, 'detail.html', context)

def register(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)
        
        if form.is_valid():

            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'You are registered with name {username}')

            return redirect('home')

    else:

        form = RegisterForm()
        
    return render(request, 'register.html', {'form' : form})

def post(request):

    if request.method == 'POST':

        form = PostForm(request.POST, request.FILES)

        if form.is_valid():

            post = form.save(commit = False)
            post.author = request.user
            post.save(request)

            return redirect('home')
    else:

        form = PostForm()
    
    return render(request, 'post.html', {'form' : form})

class UpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model =  Article
    fields = ['title', 'image', 'description', 'related', 'content']
    template_name = 'update.html'
    success_url = '/'

    def form_valid(self, form):

        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):

        article = self.get_object()

        if self.request.user == article.author:
            return True
        return False

class DeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Article
    template_name = 'delete.html'
    success_url = '/'

    def test_func(self):

        article = self.get_object()

        if self.request.user == article.author:
            return True
        return False

@login_required
def profile(request):

    user = User.objects.get(username = request.user)
    articles = Article.objects.filter(author = request.user)
    context = {
        "user": user,
        "articles": articles,
    }

    return render(request, 'profile.html', context) 