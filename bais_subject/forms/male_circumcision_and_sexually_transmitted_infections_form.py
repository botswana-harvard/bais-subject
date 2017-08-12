from django import forms

from bais_subject_form_validators.form_validations import (
    Section4FormValidator)

from ..models import MaleCircumcissionAndSexuallyTransmittedInfections


class MaleCircumcissionAndSexuallyTransmittedInfectionsForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = Section4FormValidator(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = MaleCircumcissionAndSexuallyTransmittedInfections
        fields = '__all__'
