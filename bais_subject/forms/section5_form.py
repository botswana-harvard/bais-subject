from django import forms

from ..models import Section5


class Section5Form(forms.ModelForm):

    class Meta:
        model = Section5
        fields = '__all__'
