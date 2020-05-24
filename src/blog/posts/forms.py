from django import forms
from .models import Post
from pagedown.widgets import PagedownWidget
from django_summernote.widgets import SummernoteWidget

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=PagedownWidget)
    publish = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Post
        # widgets = {
        #     'content':SummernoteWidget,
        #     'publish': forms.SelectDateWidget
        # }

        fields = [
            "title",
            "content",
            "image",
            "publish",
            "draft",
        ]

