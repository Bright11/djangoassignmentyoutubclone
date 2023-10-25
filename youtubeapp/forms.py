from .models import Video, Comment,Reply,Likevideo
from django import forms


class VideoForm(forms.ModelForm):
    class Meta:
        model=Video
        fields = ['title', 'video', 'description', 'keywords']
        video = forms.FileField(),
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': "Video Titled"}),
            # 'video': forms.FileField(),
            'description': forms.Textarea(attrs={'placeholder': 'Video description'}),
            'keywords': forms.Textarea(attrs={'placeholder': 'Keywords'}),
            }
       
        # exclude=['ownnerimage']


class ReplyForm(forms.ModelForm):
    class Meta:
        model=Reply
        fields=['reply']
        widgets = {
            'reply': forms.TextInput(attrs={'placeholder': "reply"}),
        }
        #fields=("reply",)

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['comment']
        comment=forms.TextInput(attrs={'placeholder':'comment'})