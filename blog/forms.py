from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(label="Imie",max_length=25)
    email = forms.EmailField()
    to = forms.EmailField(label="Adresat")
    comments = forms.CharField(label="Komentarz",required=False,
                               widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
