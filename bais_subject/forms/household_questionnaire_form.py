from django import forms

from bais_subject_form_validators.form_validations import (
    HouseholdQuestionnaireFormValidator)


from ..models import HouseholdQuestionnaire


class HouseholdQuestionnaireForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = HouseholdQuestionnaireFormValidator(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    # TODO: Confirm the syntax
    class Meta:
        model = HouseholdQuestionnaire
        fields = '__all__'
