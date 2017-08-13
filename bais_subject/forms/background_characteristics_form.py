from django import forms

from bais_subject_form_validators.form_validations import (
    BackgroundCharacteristicsFormValidator)

from ..models import BackgroundCharacteristics


class BackgroundCharacteristicsForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = BackgroundCharacteristicsFormValidator(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = BackgroundCharacteristics
        fields = '__all__'
