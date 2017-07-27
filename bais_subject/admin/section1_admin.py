from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..forms import Section1Form
from ..models import Section1


@admin.register(Section1)
class Section1Admin(admin.ModelAdmin):

    form = Section1Form

    radio_fields = {
        'respondent_sex': admin.VERTICAL,
        'respondent_education': admin.VERTICAL,
        'respondent_employment': admin.VERTICAL,
        'mine': admin.VERTICAL,
        'mine_occupation': admin.VERTICAL,
        'commodity': admin.VERTICAL,
        'religion': admin.VERTICAL,
        'marital_status': admin.VERTICAL,
        'living_with_spouse': admin.VERTICAL,
        'spouse_visit': admin.VERTICAL}

    fieldsets = (
        ('Section 1', {
            'fields': (
                'respondent_sex',
                'respondent_age',
                'respondent_education',
                'respondent_employment',
                'respondent_employment_other',
                'current_occupation',
                'mine',
                'mine_period',
                'mine_occupation',
                'mine_occupation_other',
                'commodity',
                'commodity_other',
                'religion',
                'religion_other',
                'marital_status',
                'respondent_marriage_age',
                'living_with_spouse',
                'spouse_visit',
                'respondent_married_years')},
         ),
        audit_fieldset_tuple
    )
