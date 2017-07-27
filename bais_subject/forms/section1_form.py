from django.forms.models import BaseModelForm

from ..models import Section1


class Section1Form(BaseModelForm):

    class Meta:
        model = Section1
        fields = '__all__'
