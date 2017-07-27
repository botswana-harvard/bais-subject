from django.forms.models import BaseModelForm

from ..models import Section4


class Section4Form(BaseModelForm):

    class Meta:
        model = Section4
        fields = '__all__'
