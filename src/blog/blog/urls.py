"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from posts import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include(('posts.urls','posts'), namespace='posts')),
    #path('',views.grand_page)
    # path("list/",views.post_list),
    # path('',views.landing_page),
    # path('create/',views.post_create),
    # path('detail/post/<int:id>/',views.post_detail, name='detail'),
    # path('update/',views.post_update),
    # path('delete/',views.post_delete),
    #path("post/", include="")
]

if (settings.DEBUG):
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)