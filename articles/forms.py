from django import forms
from django.db.models import fields
from . import models

class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Articles
        fields =['title','body','slug','thumb']