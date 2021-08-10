from django.contrib.auth import get_user_model
from django.conf import settings
from django import forms
from django.contrib.auth import *


class User(AbstractUser):
    pass


class PassChangeForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super(PassChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['old_password'].widget.attrs['placeholder'] = 'Old Password'
        self.fields['old_password'].label = ''
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'New Password'
        self.fields['new_password1'].label = ''
        self.fields[
            'new_password1'].help_text = '<ul class ="form-text text-muted small"><li>Your password can\'t be too ' \
                                         'similar to your other personal information.</li><li>Your password must ' \
                                         'contain at least 8 characters.</li><li>Your password can\'t be a commonly ' \
                                         'used password.</li><li>Your password can\'t be entirely numeric.</li></ul> '

        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['new_password2'].label = ''


class EditUserForm(UserChangeForm):
    password = forms.CharField(label="", widget=forms.TextInput(attrs={'type': 'hidden'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',)

    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'user name'
        self.fields['username'].label = ''
        self.fields[
            'username'].help_text = '<span class ="form-text text-muted"><small>Required. 150 characters or fewer. ' \
                                    'Letters, digits and @/./+/-/_ only.</small></span> '

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'first name'
        self.fields['first_name'].label = ''

        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'last name'
        self.fields['last_name'].label = ''

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'email address'
        self.fields['email'].label = ''


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control', 'placeholder': 'Email Address', 'type': 'email'}))

    class Meta:
        fields = ('username', 'email', 'password1', 'password2',)
        model = get_user_model()
