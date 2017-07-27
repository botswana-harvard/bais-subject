from django.forms.models import BaseModelForm

from ..models import Section6


class Section6Form(BaseModelForm):

    class Meta:
        model = Section6
        fields = '__all__'
