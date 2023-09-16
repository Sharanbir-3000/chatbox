from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import BotUser,FeedBack,Profile
from django import forms

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('user',)

class ChatForm(forms.ModelForm):
    class Meta:
        model = BotUser
        fields = '__all__'
        exclude = ('profile',)

class FeedbackForm(forms.Form):
    genders = (('Homo Sapiens','Homo Spains'),
    ('Women','Women'), ('Male','Male'), ('Female','Female'), ('Others','Others'))
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=genders)
    phone = forms.CharField(max_length=10)
    location = forms.CharField(max_length=50)
    descprition = forms.CharField(max_length=250)
    