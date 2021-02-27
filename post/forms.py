from django import forms
from .models import Post, Comments
from ckeditor.fields import RichTextField

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'author', 'title', 'description', 'snippet']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control', }),
            'title': forms.TextInput(attrs={'class':'form-control', }),
            'image': forms.TextInput(attrs={'class':'form-control', }),
            'author': forms.Select(attrs={'class': 'form-control', }),
            'description': forms.Textarea(attrs={'class': 'form-control', }),
            'snippet': forms.Textarea(attrs={'class': 'form-control', }),
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'image','category','snippet',]

        widgets = {
            'category': forms.Select(attrs={'class': 'form-control', }),
            'title': forms.TextInput(attrs={'class': 'form-control', }),
            'image': forms.TextInput(attrs={'class': 'form-control', }),
            'description': forms.Textarea(attrs={'class': 'form-control', }),
            'snippet': forms.Textarea(attrs={'class': 'form-control', }),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = [
            'name_lname',
            'email',
            'comment',
        ]

        widgets = {
            'name_lname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adınız Soyadınız', }),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Adres e.g. example@email.com (Email adresiniz görünmeyecektir!)', }),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Yorumunuzu Yazınız...', }),
        }