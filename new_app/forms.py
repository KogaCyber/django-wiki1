from django import forms

from .models import Category


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('titles', 'components')

        widgets = {
            'titles': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'components': forms.Textarea(attrs={
                'class': 'form-control'
            })
        }
