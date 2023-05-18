from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget


class PostCourse(forms.ModelForm):

    class Meta:
        description = forms.CharField(widget=CKEditorWidget())
        model = Course
        fields = ("title", "category", "level",
                  "description", "author")
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control placeholder-1'}),
            'category': forms.Select(attrs={'class': 'form-select form-select-sm text-dark shadow-none dropdown-menu-end'}),
            'level': forms.Select(attrs={'class': 'form-select form-select-sm text-dark shadow-none dropdown-menu-end'}),
            'author': forms.Select(attrs={'class': 'form-select form-select-sm text-dark shadow-none dropdown-menu-end'}),
        }
