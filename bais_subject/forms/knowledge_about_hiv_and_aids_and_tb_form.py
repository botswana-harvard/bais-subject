from django import forms

from bais_subject_form_validators.form_validations import (
    KnowledgeAboutHivAndAidsAndTbFormValidator)

from ..models import KnowledgeAboutHivAndAidsAndTb


class KnowledgeAboutHivAndAidsAndTbForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = KnowledgeAboutHivAndAidsAndTbFormValidator(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = KnowledgeAboutHivAndAidsAndTb
        fields = '__all__'
