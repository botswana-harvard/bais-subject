from ..models import (
    HouseholdQuestionnaireName,
    HouseholdQuestionnaireAnswers)


class HouseholdQuestionnaireForm:

    # TODO: Confirm the syntax
    class Meta:
        model = (
            HouseholdQuestionnaireName,
            HouseholdQuestionnaireAnswers)
        fields = '__all__'
