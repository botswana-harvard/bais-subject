from django import forms

from bais_subject_form_validators.form_validations import (
    Section3FormValidator)

from ..models import Section3


class Section3Form(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = Section3FormValidator(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = Section3
        fields = '__all__'
