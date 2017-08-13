from django import forms

from bais_subject_form_validators.form_validations import (
    MaleCircumcissionAndSexuallyTransmittedInfectionsFormValidator)

from ..models import MaleCircumcissionAndSexuallyTransmittedInfections


class MaleCircumcissionAndSexuallyTransmittedInfectionsForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = MaleCircumcissionAndSexuallyTransmittedInfectionsFormValidator(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = MaleCircumcissionAndSexuallyTransmittedInfections
        fields = '__all__'
