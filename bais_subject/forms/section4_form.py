from django import forms

from bais_subject_form_validators.form_validations import (
    Section4FormValidator)

from ..models import Section4


class Section4Form(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = Section4FormValidator(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = Section4
        fields = '__all__'
