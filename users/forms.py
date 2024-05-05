from django import forms
from django.contrib.auth.forms import AuthenticationForm # джанго предоставляет форму, от нее можно наследоваться, создавать готовые формы
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'plaseholder':'Enter user name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'plaseholder':'Enter password'}))  
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control'

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'plaseholder':'Enter first name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'plaseholder':'Enter first name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'plaseholder':'Enter first name'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'plaseholder':'Enter first name'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'plaseholder':'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'plaseholder':'Confirm password'}))
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field_name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control'

