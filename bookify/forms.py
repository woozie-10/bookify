from django import forms
from .models import Book, Review

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'description', 'file', 'cover']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Book Name', 'class': 'form-input', 'required': 'true'}),
            'author': forms.TextInput(attrs={'placeholder': 'Author', 'required': 'true', 'class': 'form-input',}),
            'description': forms.Textarea(attrs={'placeholder': 'Description', 'rows': 6, 'required': 'true', 'class': 'form-input',}),
            'file': forms.ClearableFileInput(attrs={'accept': 'application/pdf, .epub, .mobi', 'class': 'file-input', 'required': 'true', 'class': 'file-input'}),
            'cover': forms.ClearableFileInput(attrs={'accept': 'image/*', 'class': 'file-input', 'required': 'true','class': 'file-input'}),
        }
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Review...', 'rows': 8, 'required': 'true', 'class': 'form-input'}),
        }