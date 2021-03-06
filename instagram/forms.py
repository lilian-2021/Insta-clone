from django import forms
from .models import Comment, Image
from users.models import Profile


class AddPostForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={

        'id': 'img1', 'class': 'imgs2'

    }))

    class Meta:
        model = Image
        fields = ['name','caption','image']        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment        
        fields=['comment']
        