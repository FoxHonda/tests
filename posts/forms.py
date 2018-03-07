from django import forms
from . import models

class PostForm(forms.ModelForm):
	
	class Meta:
		model = models.Post
		fields = ['title','image','description','posttext','theme']			
		widgets = {
            'title': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Enter image'}),
            'description': forms.widgets.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
            'posttext': forms.widgets.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter text'}),
            'theme': forms.widgets.Select(attrs={'class': 'form-control', 'placeholder': 'Enter theme'})
        }