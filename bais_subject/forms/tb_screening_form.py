from django import forms


from bais_subject_form_validators.form_validations import (
    TBScreeningFormValidator)

from ..models import TBScreening


class TBScreeningForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = TBScreeningFormValidator(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = TBScreening
        fields = '__all__'
