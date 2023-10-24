from django import forms
from .models import Post

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    comment = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows':'5', 'cols':'50'}))

class NewPost(forms.ModelForm): 
    class Meta:
        model = Post
        fields = ['title', 'body', 'status', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'cols': '50', 'rows': '8'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }
