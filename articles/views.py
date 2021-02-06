from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Articles
from django.contrib.auth.decorators import login_required
from .import forms

def article_list(request):
    articles = Articles.objects.all().order_by('date')
    return render(request,'articles/articles_list.html',{'articles':articles})

def article_detail(request,slug):
    article = Articles.objects.get(slug=slug)
    return render(request,'articles/articles_details.html',{'article':article})



@login_required(login_url='accounts:login')
def article_create(request):
    if request.method is "POST":
        form = forms.CreateArticle(request.POST,request.FILES,request.user)
        if form.is_valid():
            #save Article to db
            # form.save() #will save the data to database but won't have any user 

            instance = form.save()  # using this parameter saving data with the user
            instance.authur = request.User
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
        return render(request,'articles/article_create.html',{'form':form})