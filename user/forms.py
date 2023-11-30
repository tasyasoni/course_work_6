from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from user.models import User


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'phone',)


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)


class UserProfileForm(StyleFormMixin, UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'avatar', 'country',)

    def __init__(self, *args, **kwargs):  # убирает информацию про кодировку пароля в профиле
        super().__init__(*args, **kwargs)
        print(self.fields)

        self.fields['password'].widget = forms.HiddenInput()





