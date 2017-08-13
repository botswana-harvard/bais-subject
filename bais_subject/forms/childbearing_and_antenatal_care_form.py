from django import forms

from bais_subject_form_validators.form_validations import (
    ChildbearingAndAntenatalCareFormValidator)

from ..models import ChildbearingAndAntenatalCare


class ChildbearingAndAntenatalCareForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = ChildbearingAndAntenatalCareFormValidator(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = ChildbearingAndAntenatalCare
        fields = '__all__'
