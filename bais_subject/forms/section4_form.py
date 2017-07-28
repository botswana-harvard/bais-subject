from django import forms

from ..models import Section4


class Section4Form(forms.ModelForm):

    class Meta:
        model = Section4
        fields = '__all__'
