from django import forms

from ..models import Section8


class Section8Form(forms.ModelForm):

    class Meta:
        model = Section8
        fields = '__all__'
