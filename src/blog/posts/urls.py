from django.urls import path,include,reverse
from django.contrib import admin
from . import views
app_name='posts'
urlpatterns=[
    path("list/",views.post_list, name='list'),
    path('',views.landing_page),
    path('create/',views.post_create),
    #path('posts/<int:id>/',views.post_detail, name= 'detail'),
    path('<slug:slug>/',views.post_detail, name='post_detail'),
    path('<slug:slug>/edit/',views.post_update, name='update'),
    path('<slug:slug>/delete/',views.post_delete),
]
