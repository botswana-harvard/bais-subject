from django.forms.models import BaseModelForm

from ..models import Section3


class Section3Form(BaseModelForm):

    class Meta:
        model = Section3
        fields = '__all__'
