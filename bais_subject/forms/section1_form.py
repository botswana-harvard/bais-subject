from django import forms

from ..models import Section1


class Section1Form(forms.ModelForm):

    class Meta:
        model = Section1
        fields = '__all__'
