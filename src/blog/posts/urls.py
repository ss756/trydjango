from django.urls import path,include,reverse
from django.contrib import admin
from . import views
from django.views.generic import FormView
from .views import SearchPageView, HomePageView
from .forms import PostForm
app_name='posts'
urlpatterns=[
    path("list/" , views.post_list, name='list'),
    path('search/', SearchPageView.as_view(), name='search_results'),
    path('create/', views.post_create, name ='create'),
    #path('posts/<int:id>/',views.post_detail, name= 'detail'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit/', views.post_update, name='update'),
    path('<slug:slug>/delete/', views.post_delete),
    path('', HomePageView.as_view(),name='home')
]
#views.post_create),