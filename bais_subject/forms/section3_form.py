from django import forms

from ..models import Section3


class Section3Form(forms.ModelForm):

    class Meta:
        model = Section3
        fields = '__all__'
