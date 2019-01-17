from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:

        model = Blog
        fields = ('title', 'text_area')
        widgets = {'title': forms.TextInput(attrs={'placeholder': 'Title',
                                                   'class': 'form-control'}),
                   'text_area': forms.Textarea(attrs={'placeholder': 'Enter a desc',
                                                      'class': 'form-control'}),

}