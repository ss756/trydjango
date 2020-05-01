from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,HttpResponseRedirect, Http404
from django.contrib import messages
from django.urls import reverse
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.shortcuts import render
from urllib.parse import quote_plus
from django.utils import timezone



# Create your views here.
def post_create(request, *args, **kwargs):
    form = PostForm(request.POST or None, request.FILES or None)
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    if form.is_valid():
        instance= form.save(commit=False)
        # print(form.cleaned_data.get("title"))
        # print(form.cleaned_data.get("content"))
        instance.save()
        messages.success(request,"Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    # if (request.method=="POST"):
    #     print(request.POST.get("content"))
    #     print(request.POST.get("title"))
    context = {
        "form": form
    }
    return render(request, "post_form.html", context)

def post_detail(request, slug, *args, **kwargs):
    # return HttpResponse('<h1> Post Details are below  </h1')
    instance = get_object_or_404(Post, slug=slug)
    if instance.draft :
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    share_string=quote_plus(instance.content)
    boo = request.user.is_authenticated
    context = {
            "title": instance.title,
            "instance": instance,
            "share_string": share_string,
        }
    return render(request, "post_detail.html", context)


def post_list(request, *args, **kwargs):
    # # return HttpResponse('<h1> Post list  </h1')
    # boo = request.user.is_authenticated
    # if (boo):
    #     context = {
    #         "title": "My User List Is Working List"
    #     }
    # else:
    #     context={
    #         "title": "My Post List is working"
    #     }
    queryset_list: object = Post.objects.active().order_by('-timestamp')
    if request.user.is_staff or request.user.is_superuser:
        queryset_list: object= Post.objects.all().order_by('timestamp')
    #queryset_list: object = Post.objects.filter(draft=False).filter(publish__lte=timezone.now())
    #queryset_list: object = Post.objects.filter(draft=False)
    paginator = Paginator(queryset_list, 2)  # show 9 contacts per page
    page_request_var="page"
    page = request.GET.get(page_request_var)

    try:
        queryset= paginator.page(page)
    except PageNotAnInteger:
        # If the page is not an integer, deliver first page
        queryset = paginator.page(1)
    except EmptyPage:
        # if page is out of range (e.g 9999) deliver last page of result
        queryset = paginator.page(paginator.num_pages)
    context = {
        "object_list": queryset,
        "title": "List",
        "page_request_var":page_request_var
    }
    return render(request, "post_list.html", context)


def post_update(request, slug=None):
    instance=get_object_or_404(Post,slug=slug)
    form=PostForm(request.POST or None,request.FILES or None,instance=instance)
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    if form.is_valid():
        instance= form.save(commit=False)
        instance.save()
        # message success
        messages.success(request,"<A href='/posts/list/'>Item</A>Saved", extra_tags="html_update")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.title,
        "instance": instance,
        "form":form
    }
    return render(request,"post_form.html",context)



def post_delete(request,slug=None):
    if not request.user.is_superuser or not request.user.is_authenticated:
        raise Http404
    instance=get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request,"Successfully Deleted")
    return redirect("posts:list")




def landing_page(request, *args, **kwargs):
    print(request.user.is_authenticated)
    return HttpResponse("<h1> Landing Page ..... Under Construction ")


def grand_page(request, *args, **kwargs):
    return HttpResponse("<h1> Super Hero Landing </h1>  ")


