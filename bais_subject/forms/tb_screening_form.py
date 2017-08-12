from django import forms

from ..models import TBScreening


class TBScreeningForm(forms.ModelForm):

    class Meta:
        model = TBScreening
        fields = '__all__'
