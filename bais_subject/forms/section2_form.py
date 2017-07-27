from django.forms.models import BaseModelForm

from ..models import Section2


class Section2Form(BaseModelForm):

    class Meta:
        model = Section2
        fields = '__all__'
