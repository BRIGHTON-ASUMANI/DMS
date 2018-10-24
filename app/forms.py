from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class EditProfileForm(UserCreationForm):
    password1 = forms.CharField(label='', widget = forms.TextInput(attrs={'type':'hidden'}))
    password2 = forms.CharField(label='', widget = forms.TextInput(attrs={'type':'hidden'}))
    email = forms.EmailField(label='',widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'email address'}))
    first_name = forms.CharField(label='',max_length=100, widget = forms.TextInput(attrs={'class':'form-control' , 'placeholder':'first name'}))
    last_name = forms.CharField(label='',max_length=100, widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'last name'}))
    # fav_color = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = ""

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = ""

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'confirm password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = ""


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='',widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'email address'}))
    first_name = forms.CharField(label='',max_length=100, widget = forms.TextInput(attrs={'class':'form-control' , 'placeholder':'first name'}))
    last_name = forms.CharField(label='',max_length=100, widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'last name'}))
    # fav_color = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1','password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = ""



        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = ""

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'confirm password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = ""
