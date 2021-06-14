from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields= ('title', 'text')

class UploadFileForm(forms.Form):
    file = forms.FileField()

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('abc','photo',)