from django import forms

from ..models import ChildbearingAndAntenatalCare


class ChildbearingAndAntenatalCareForm(forms.ModelForm):

    class Meta:
        model = ChildbearingAndAntenatalCare
        fields = '__all__'
