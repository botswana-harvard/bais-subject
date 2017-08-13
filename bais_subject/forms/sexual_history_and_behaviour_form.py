from django import forms

from bais_subject_form_validators.form_validations import (
    SexualHistoryAndBehaviourFormValidator)

from ..models import SexualHistoryAndBehaviour


class SexualHistoryAndBehaviourForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = SexualHistoryAndBehaviourFormValidator(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = SexualHistoryAndBehaviour
        fields = '__all__'
