from django import forms

from ..models import AttitudesTowardsPeople


class AttitudesTowardsPeopleForm(forms.ModelForm):

    class Meta:
        model = AttitudesTowardsPeople
        fields = '__all__'
