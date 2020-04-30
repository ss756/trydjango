from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
# MVC  Model View Controller
def upload_location(instance,filename):
    return "{}/{}".format(instance.slug,filename)
User= settings.AUTH_USER_MODEL
class Post(models.Model):
    user=models.ForeignKey(User,default=1,null=True, on_delete=models.SET_NULL)
    title=models.CharField(max_length=120)
    slug=models.SlugField(unique=True)
    content=models.TextField()
    image=models.ImageField(upload_to=upload_location,width_field='width_field',height_field='height_field')
    width_field=models.IntegerField(default=0)
    height_field=models.IntegerField(default=0)
    timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)
    updated=models.DateTimeField(auto_now=True,auto_now_add=False)
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("posts:post_detail",kwargs={"slug": self.slug})
        #return "/detail/post/%s/"%(self.id)
    class Meta:
        ordering=["-timestamp","-updated"]

def create_slug(instance,new_slug=None):
    slug=slugify(instance.title)
    if new_slug is not None:
        slug=new_slug
    qs=Post.objects.filter(slug=slug).order_by("-id")
    exists= qs.exists()
    if exists:
        new_slug ="{}-{}".format(slug, qs.first().id)
        return create_slug(instance, new_slug= new_slug)
    return slug

def pre_save_post_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug =create_slug(instance)
pre_save.connect(pre_save_post_receiver, sender=Post)













