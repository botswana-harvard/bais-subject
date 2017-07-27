from django.forms.models import BaseModelForm

from ..models import HouseholdQuestionnaire


class HouseholdQuestionnaireForm(BaseModelForm):

    # TODO: Confirm the syntax
    class Meta:
        model = HouseholdQuestionnaire
        fields = '__all__'
