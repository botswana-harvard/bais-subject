from django import forms

from ..models import Section2


class Section2Form(forms.ModelForm):

    class Meta:
        model = Section2
        fields = '__all__'
