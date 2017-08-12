from django import forms

from ..models import KnowledgeAboutHivAndAidsAndTb


class KnowledgeAboutHivAndAidsAndTbForm(forms.ModelForm):

    class Meta:
        model = KnowledgeAboutHivAndAidsAndTb
        fields = '__all__'
