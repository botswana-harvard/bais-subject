from django import forms


from ..models import HouseholdQuestionnaire


class HouseholdQuestionnaireForm(forms.ModelForm):

    # TODO: Confirm the syntax
    class Meta:
        model = HouseholdQuestionnaire
        fields = '__all__'
