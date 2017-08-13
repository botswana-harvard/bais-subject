from django import forms

from bais_subject_form_validators.form_validations import (
    AlcoholConsumptionAndSubstanceUseFormValidator)

from ..models import AlcoholConsumptionAndSubstanceUse


class AlcoholConsumptionAndSubstanceUseForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = AlcoholConsumptionAndSubstanceUseFormValidator(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = AlcoholConsumptionAndSubstanceUse
        fields = '__all__'
