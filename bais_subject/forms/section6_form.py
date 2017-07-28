from django import forms

from ..models import Section6


class Section6Form(forms.ModelForm):

    class Meta:
        model = Section6
        fields = '__all__'
