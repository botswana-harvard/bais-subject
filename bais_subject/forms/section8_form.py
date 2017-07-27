from django.forms.models import BaseModelForm

from ..models import Section8


class Section8Form(BaseModelForm):

    class Meta:
        model = Section8
        fields = '__all__'
