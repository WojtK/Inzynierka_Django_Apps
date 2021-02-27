from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    imie = forms.CharField(max_length=25)
    email = forms.EmailField()
    do = forms.EmailField()
    komentarz = forms.CharField(required=False,
                                widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
