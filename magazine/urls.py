from django.urls import path, re_path
from . import views
from django.contrib.auth import views as previews
from .views import DeleteView, UpdateView

urlpatterns = [
    re_path(r'^$', views.home, name = "home"),
    re_path(r'^(?P<article_id>[0-9]+)/$', views.detail, name = "detail"),
    re_path(r'^register/$', views.register, name = 'register'),
    re_path(r'^post/$', views.post, name = 'post'),
    re_path(r'^(?P<pk>[0-9]+)/update/$', UpdateView.as_view(), name = "update"),
    re_path(r'^(?P<pk>[0-9]+)/delete/$', DeleteView.as_view(), name = "delete"),
    re_path(r'^profile/$', views.profile, name = "profile"),
    re_path(r'^login/$', previews.LoginView.as_view(template_name = 'login.html'), name = 'login'),
    re_path(r'^logout/$', previews.LogoutView.as_view(template_name = 'logout.html'), name = 'logout'),
]