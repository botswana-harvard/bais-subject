from django.forms.models import BaseModelForm

from ..models import Section5


class Section5Form(BaseModelForm):

    class Meta:
        model = Section5
        fields = '__all__'
