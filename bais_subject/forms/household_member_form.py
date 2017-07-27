from django.forms.models import BaseModelForm

from ..models import HouseholdMember


class HouseholdMemberForm(BaseModelForm):

    class Meta:
        model = HouseholdMember
        fields = '__all__'
