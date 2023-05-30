from django import forms
import django_filters
from django_filters import CharFilter, ModelChoiceFilter
from app.models import *


class CourseFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains',
                       widget=forms.TextInput(attrs={'class': 'form-control form-control-sm placeholder-dark border-end-0 shadow-non', 'placeholder': 'Search your course'}))

    class Meta:
        model = Course
        fields = ["category", "title"]
