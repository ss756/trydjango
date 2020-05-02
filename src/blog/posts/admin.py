from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title",'__unicode__','updated','timestamp']
    list_display_links = ["updated"]
    list_filter = ["updated","timestamp"]
    list_editable = ["title"]
    class Meta:
        model = Post

admin.site.register(Post,PostModelAdmin)

