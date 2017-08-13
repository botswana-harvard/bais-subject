from django import forms

from bais_subject_form_validators.form_validations import (
    AttitudesTowardsPeopleFormValidator)

from ..models import AttitudesTowardsPeople


class AttitudesTowardsPeopleForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = AttitudesTowardsPeopleFormValidator(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = AttitudesTowardsPeople
        fields = '__all__'
