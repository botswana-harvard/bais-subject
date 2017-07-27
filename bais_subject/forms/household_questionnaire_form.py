from django.forms.models import BaseModelForm

from ..models import (
    HouseholdQuestionnaireName,
    HouseholdQuestionnaireAnswers)


class HouseholdQuestionnaireForm(BaseModelForm):

    # TODO: Confirm the syntax
    class Meta:
        model = (
            HouseholdQuestionnaireName,
            HouseholdQuestionnaireAnswers)
        fields = '__all__'
