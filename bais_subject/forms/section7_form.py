from django import forms

from ..models import Section7


class Section7Form(forms.ModelForm):

    class Meta:
        model = Section7
        fields = '__all__'
