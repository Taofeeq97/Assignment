from django import forms
from .models import Diversity, Module

class DiversityForm(forms.ModelForm):
    class Meta:
        model = Diversity
        fields = ['ethnic_group', 'student_count']


class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['name', 'description']
