from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import *


# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))

            else:
                return redirect('CTAC:home')
        else:
            return redirect('account:login')
    else:
        return render(request, "login.html", {})


def logout_user(request):
    logout(request)
    return redirect('CTAC:home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('CTAC:home')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'signup.html', context)


def edit_user(request):
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)

            return redirect('home')
    else:
        form = EditUserForm(instance=request.user)
    context = {'form': form}
    return render(request, 'update.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)

            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request, 'passewordchange.html', context)
