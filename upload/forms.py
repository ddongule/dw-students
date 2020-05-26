from django import forms
from .models import Assignment

class AssignmentForm(forms.ModelForm):
    name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class':'input-form', 'placeholder':'이름을 꼭! 써주세요'}))
    image = forms.ImageField(required=True, label="", widget=forms.ClearableFileInput(attrs={'class':'filefield'}))

    class Meta:
        model = Assignment
        fields = ['name', 'image']
    