from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth, Group
from django.contrib.auth import authenticate
from django.contrib import messages
from accounts.decorators import unauthenticated_user,allowed_users, admin_only
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required (login_url= 'login')
def cart (request):
    return render (request,'cart/cart.html')