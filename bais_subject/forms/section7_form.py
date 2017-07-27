from django.forms.models import BaseModelForm

from ..models import Section7


class Section7Form(BaseModelForm):

    class Meta:
        model = Section7
        fields = '__all__'
