from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm, ProfileForm
from .models import Event, Profile
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.edit import UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
import datetime as dt
# Create your views here.

@login_required(login_url='/login')
def profile(request):
    profile =Profile.objects.filter(user=request.user.id)
    events =Event.objects.all()

    return render(request, 'profile.html', { "events":events, "profile": profile})

@login_required(login_url='/login')
def dump(request,pk):
    profile =Profile.objects.filter(user=request.user.id)
    project =Project.objects.filter(user=request.user.id)
    # commented = CommentForm()
    return render(request,'dump.html',{"profile": profile, "project": project})

@login_required( login_url='/login' )
def create(request):
    current_user=request.user
    if request.method == 'POST':
        form=ProfileForm( request.POST , request.FILES )
        if form.is_valid( ):
            update=form.save( commit=False )
            update.user=current_user
            update.save( )
            return redirect( 'profile' )
    else:
        form=ProfileForm( )
    return render( request , 'create.html' , {"form": form} )



@login_required( login_url='/login' )
def edit(request):
    current_user=request.user
    if request.method == 'POST':
        form=ProfileForm( request.POST,request.FILES,instance=request.user.profiile)
        if form.is_valid():
            form.save( )
            return redirect( 'profile' )
    else:
        form=ProfileForm( )
    return render( request , 'edit.html' , {"form": form} )




class ProfileUpdate(UpdateView):
   model= Profile
   template_name = 'edit.html'
   fields = ['picture','bio','phone_number']


class ProfileDelete(DeleteView):
   model=Profile
   success_url = reverse_lazy('profile')




def home(request):
    print(request.user.id)
    print(dt.datetime.now().strftime('%H:%M:%S'))
    return render(request, 'home.html', {} )

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
        return render(request, 'login.html', {} )

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
    return render(request, 'register.html',context)

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
    return render(request, 'edit_profile.html',context)

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
    return render(request, 'change_password.html',context)
