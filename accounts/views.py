from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth,Group
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.decorators import login_required

# Create your views here.

@unauthenticated_user
def register (request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name = first_name,last_name=last_name)
                user.save()
                group = Group.objects.get (name='customer')
                user.groups.add(group)
                messages.success(request, 'Account is successfully created')
                return redirect ('login')
        else:
            messages.warning(request, 'Password does not match')
            return redirect ('register')
    else:
        return render (request,'accounts/register.html')

@unauthenticated_user
def login (request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user= authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            #messages.success(request,'User successfully logged in.')
            return redirect('/')
        else:
            messages.warning(request,'Username or Password is incorrect')
            return redirect('login')
    else:
        return render (request,'accounts/login.html')

def logout(request):
    auth.logout(request)
    #messages.warning(request,'User Logged out')
    return redirect('/')

@login_required(login_url='login')
def profile(request):
    users= User.objects.all
    return render (request,'accounts/profile.html', {'users': users})

@login_required(login_url='login')

def edit_profile (request,id):
    users =User.objects.get(id = id)
    context = {'users':users}
    return render (request,'accounts/edit-profile.html',context)

@login_required(login_url='login')

def update_profile (request,id):
    user =User.objects.get(id = id)
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.username = request.POST['username']
    user.email = request.POST['email']
    user.save()
    messages.info(request,'SAVE CHANGES')
    return redirect ('profile')
