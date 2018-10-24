from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm

# Create your views here.
def home(request):
    return render(request, 'registration/home.html', {} )

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You have been logged in' ))
            return redirect('home')
        else:
            messages.success(request, ('error logging in - please try again' ))
            return redirect('login')
    else:
        return render(request, 'registration/login.html', {} )

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out' ))
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ('You have been registered' ))
            return redirect('home')

    else:
        form = SignUpForm()
    context = {'form': form }
    return render(request, 'registration/register.html',context)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('You have editted your profile' ))
            return redirect('home')

    else:
        form = EditProfileForm(instance=request.user)
    context = {'form': form }
    return render(request, 'registration/edit_profile.html',context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, ('You have password has been changed' ))
            return redirect('home')

    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form }
    return render(request, 'registration/change_password.html',context)
