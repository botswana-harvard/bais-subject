from django import forms

from bais_subject_form_validators.form_validations import (
    Section1FormValidator)

from ..models import Section1


class Section1Form(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = Section1FormValidator(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = Section1
        fields = '__all__'
