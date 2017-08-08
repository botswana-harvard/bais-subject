from django import forms

from bais_subject_form_validators.form_validations import (
    Section2FormValidator)

from ..models import Section2


class Section2Form(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = Section2FormValidator(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = Section2
        fields = '__all__'
