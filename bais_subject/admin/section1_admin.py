from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import bais_subject_admin
from ..forms import Section1Form
from ..models import Section1


@admin.register(Section1, site=bais_subject_admin)
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
        'respondent_age': admin.VERTICAL,
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
                'respondent_age',)},
         ),
        audit_fieldset_tuple
    )
