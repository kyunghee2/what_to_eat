from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from .forms import CustomUserChangeForm
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model

def signup(request):
    if request.user.is_authenticated:
        return redirect('restaurant:index')

    if request.method=='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('restaurant:index')
    else:
        form = CustomUserCreationForm
    context ={'form':form}
    return render(request,'accounts/auth_form.html',context)

def login(request):
    if request.user.is_authenticated:
        return redirect('restaurant:index')

    if request.method =='POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('restaurant:index')
    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(request,'accounts/login.html',context)

def logout(request):
    auth_logout(request)
    return redirect('restaurant:index')

#회원정보 수정
@login_required #로그인 회원만 접근가능
def update(request):
    if request.method =='POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('restaurant:index')
    else:
        #form = UserChangeForm(instance=request.user)
        form = CustomUserChangeForm(instance=request.user)

    context = {'form':form}
    return render(request,'accounts/auth_form.html',context)

#비밀번호 변경
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('restaurant:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form':form}
    return render(request,'accounts/auth_form.html',context)

# 회원탈퇴 - 로그인한 사람만 보임
@require_POST
def delete(request):
    request.user.delete()
    return redirect('restaurant:index')

#프로필
def profile(request, username):
    person = get_object_or_404(get_user_model(),username=username)
    context = {'person': person}
    return render(request, 'accounts/profile.html',context)
