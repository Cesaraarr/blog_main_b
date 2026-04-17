from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        windgets = { 
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'tu nombre'
            }),
            'email': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 1,
                'placeholder': 'tu email'
            }),
              'body': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': 'Escribe tu comentario'
            }),
        }