from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.

def signup_view(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html',{'form':form})

def login_view(request):
    # if login is True:
    #     return redirect('articles:list')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')

    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form': form})


def logout_view(request):
    if request.method is not 'POST':
        logout(request)
        messages.info(request, "Logged out successfully!")
    return redirect('home')
    
