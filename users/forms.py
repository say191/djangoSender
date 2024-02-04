from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User
from django import forms


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('FIO', 'phone', 'email', 'password1', 'password2')


class UserVerifyForm(forms.Form):
    verify_token = forms.CharField(max_length=5)


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'FIO', 'phone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()


class UserChangePassForm(forms.Form):
    new_password1 = forms.CharField(max_length=10)
    new_password2 = forms.CharField(max_length=10)

    def clean(self):
        data = self.cleaned_data
        if not('new_password1' in data.keys() or 'new_password2' in data.keys()):
            raise forms.ValidationError('Fill out missing fields ')
        password1 = data['new_password1']
        password2 = data['new_password2']
        if password1.isalpha() or password1.isdigit():
            raise forms.ValidationError("Password must consist of letters and numbers")
        elif len(password1) < 6:
            raise forms.ValidationError("Password must be 6 characters long")
        elif password1 != password2:
            raise forms.ValidationError("Passwords must be the same")


class UserForgotPassForm(forms.Form):
    email = forms.CharField(max_length=30)