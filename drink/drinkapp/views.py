from django.shortcuts import render
from .models import *
from django.utils import timezone
from .forms import *
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .forms import UploadFileForm
import simplejson
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

def post_new(request):
    if request.method=="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
        return redirect(index)
    else:
        form = PostForm()
        return render(request,'drinkapp/post_edit.html', {'form': form})

def login(request):
    if request.method!="POST":
        return render(request, 'drinkapp/accounts/login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect(index)
        else:
            return redirect(index)


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if not password==password2:
            return redirect(index)
        for i in User.objects.all():
            if username == i.username:
                return redirect(index)
        user = User.objects.create_user(username=username, email='jlennon@beatles.com', password=password2)

        profile = UserProfile()
        
        user.save()
        profile.user = user
        profile.save()
        
        autologin(request, user)
        return redirect(index)
    else:
        return render(request, "drinkapp/accounts/register.html")
    

def autologin(request, user: User):
    auth.login(request, user)
    #redirect(post_list)

def logout(request):
    auth.logout(request)
    return redirect(index)

def room(request, room_name):
    user = request.user
    
    return render(request, 'drinkapp/room.html', {
        'room_name': room_name,
        #'user': request.user
    })



def profile(request):
    user = request.user
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            if profile.photo != 'default':
                user.userprofile.photo = profile.photo
                print('should be changed')
            user.userprofile.abc = profile.abc
            user.userprofile.save()
                
        return redirect(index)
    else:
        profile_form = UserProfileForm(initial={'abc': user.userprofile.abc, 'photo': user.userprofile.photo})
        return render(request, 'drinkapp/profile.html', {'pf': profile_form})



    

def index(request):
    user = request.user
    posts = Post.objects.all()
    if user.is_authenticated:
        return render(request,'drinkapp/index.html', {'posts': posts, 'user': user, 'photo': user.userprofile.photo} )
    else:
        return render(request,'drinkapp/index.html', {'posts': posts} )
        


def ost_new(request):
    if request.method=="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
        return redirect(index)
    else:
        form = PostForm()
        return render(request,'drinkapp/post_edit.html', {'form': form})
